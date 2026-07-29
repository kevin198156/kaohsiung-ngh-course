#!/usr/bin/env python3
"""Validate the static GitHub Pages site using only Python's standard library."""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_HTML = [
    ROOT / "index.html",
    ROOT / "instructor.html",
    ROOT / "faq.html",
    ROOT / "course-guide.html",
    ROOT / "registration-guide.html",
    ROOT / "policy.html",
    ROOT / "404.html",
]
MAIN_HTML = PUBLIC_HTML[:-1]
EXPECTED_BASE = "https://kevin198156.github.io/kaohsiung-ngh-course/"
OFFICIAL_URL = "https://eec.nuk.edu.tw/course_detail.php?sn=1059"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.attrs: list[tuple[str, dict[str, str]]] = []
        self.links: list[str] = []
        self.images: list[dict[str, str]] = []
        self.json_ld: list[str] = []
        self.h1_count = 0
        self.title_parts: list[str] = []
        self._in_title = False
        self._in_json_ld = False
        self._json_buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {key: value or "" for key, value in attrs}
        self.attrs.append((tag, data))
        if tag == "a" and data.get("href"):
            self.links.append(data["href"])
        elif tag == "img":
            self.images.append(data)
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "title":
            self._in_title = True
        elif tag == "script" and data.get("type") == "application/ld+json":
            self._in_json_ld = True
            self._json_buffer = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        elif tag == "script" and self._in_json_ld:
            self._in_json_ld = False
            self.json_ld.append("".join(self._json_buffer).strip())

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_parts.append(data)
        if self._in_json_ld:
            self._json_buffer.append(data)

    @property
    def title(self) -> str:
        return " ".join(part.strip() for part in self.title_parts if part.strip())

    def first_attr(self, tag: str, **matches: str) -> dict[str, str] | None:
        for current_tag, attrs in self.attrs:
            if current_tag == tag and all(attrs.get(key) == value for key, value in matches.items()):
                return attrs
        return None


def fail(errors: list[str], page: Path | str, message: str) -> None:
    name = page.name if isinstance(page, Path) else page
    errors.append(f"{name}: {message}")


def local_target(page: Path, href: str) -> Path | None:
    if not href or href.startswith(("#", "mailto:", "tel:")):
        return None
    parsed = urlparse(href)
    if parsed.scheme in {"http", "https"}:
        return None
    clean = parsed.path
    if clean.startswith("/kaohsiung-ngh-course/"):
        clean = clean.removeprefix("/kaohsiung-ngh-course/")
    elif clean.startswith("/"):
        return ROOT / clean.removeprefix("/")
    if not clean:
        clean = "index.html"
    return ROOT / clean


def main() -> int:
    errors: list[str] = []
    titles: dict[str, str] = {}
    descriptions: dict[str, str] = {}
    canonicals: set[str] = set()

    for page in PUBLIC_HTML:
        if not page.exists():
            fail(errors, page, "檔案不存在")
            continue
        text = page.read_text(encoding="utf-8")
        parser = PageParser()
        parser.feed(text)

        html_tag = parser.first_attr("html")
        if not html_tag or html_tag.get("lang") != "zh-Hant-TW":
            fail(errors, page, "html lang必須是zh-Hant-TW")
        if parser.h1_count != 1:
            fail(errors, page, f"必須只有一個H1，目前為{parser.h1_count}")
        if not parser.title:
            fail(errors, page, "缺少title")
        elif parser.title in titles:
            fail(errors, page, f"title與{titles[parser.title]}重複")
        else:
            titles[parser.title] = page.name

        description = parser.first_attr("meta", name="description")
        content = description.get("content", "").strip() if description else ""
        if not content:
            fail(errors, page, "缺少meta description")
        elif content in descriptions:
            fail(errors, page, f"description與{descriptions[content]}重複")
        else:
            descriptions[content] = page.name

        canonical = parser.first_attr("link", rel="canonical")
        canonical_url = canonical.get("href", "") if canonical else ""
        if not canonical_url.startswith(EXPECTED_BASE):
            fail(errors, page, "canonical不是預定GitHub Pages網址")
        elif canonical_url in canonicals:
            fail(errors, page, "canonical重複")
        else:
            canonicals.add(canonical_url)

        robots_meta = parser.first_attr("meta", name="robots")
        if robots_meta and "noindex" in robots_meta.get("content", "").lower():
            fail(errors, page, "不得包含noindex")

        if page in MAIN_HTML and OFFICIAL_URL not in parser.links:
            fail(errors, page, "缺少高雄大學正式課程連結")

        for image in parser.images:
            if "alt" not in image:
                fail(errors, page, f"圖片{image.get('src', '')}缺少alt")
            if not image.get("width") or not image.get("height"):
                fail(errors, page, f"圖片{image.get('src', '')}缺少width/height")
            src = image.get("src", "")
            target = local_target(page, src)
            if target and not target.exists():
                fail(errors, page, f"圖片不存在：{src}")

        for href in parser.links:
            if href.startswith("http://"):
                fail(errors, page, f"外部連結必須使用HTTPS：{href}")
            target = local_target(page, href)
            if target and not target.exists():
                fail(errors, page, f"內部連結不存在：{href}")

        for index, block in enumerate(parser.json_ld, start=1):
            try:
                json.loads(block)
            except json.JSONDecodeError as exc:
                fail(errors, page, f"JSON-LD #{index}無法解析：{exc}")

        if "【待提供" in text or "【待確認" in text:
            fail(errors, page, "對外HTML不得出現待補占位文字")

    try:
        course_data = json.loads((ROOT / "content/course-data.json").read_text(encoding="utf-8"))
        if course_data["course"]["officialUrl"] != OFFICIAL_URL:
            fail(errors, "course-data.json", "正式課程網址不正確")
        if course_data["site"]["baseUrl"] != EXPECTED_BASE:
            fail(errors, "course-data.json", "baseUrl不正確")
    except (OSError, KeyError, json.JSONDecodeError) as exc:
        fail(errors, "course-data.json", f"無法解析集中資料：{exc}")

    try:
        tree = ET.parse(ROOT / "sitemap.xml")
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locations = [node.text for node in tree.findall(".//sm:loc", ns)]
        expected = [
            EXPECTED_BASE,
            EXPECTED_BASE + "instructor.html",
            EXPECTED_BASE + "faq.html",
            EXPECTED_BASE + "course-guide.html",
            EXPECTED_BASE + "registration-guide.html",
            EXPECTED_BASE + "policy.html",
        ]
        if locations != expected:
            fail(errors, "sitemap.xml", "網址清單或順序不正確")
        for node in tree.findall(".//sm:lastmod", ns):
            if not node.text or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", node.text):
                fail(errors, "sitemap.xml", "lastmod格式必須為YYYY-MM-DD")
    except (OSError, ET.ParseError) as exc:
        fail(errors, "sitemap.xml", f"XML無法解析：{exc}")

    robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
    for agent in ("Googlebot", "Bingbot", "OAI-SearchBot"):
        pattern = rf"User-agent:\s*{re.escape(agent)}\s+Allow:\s*/"
        if not re.search(pattern, robots, flags=re.IGNORECASE):
            fail(errors, "robots.txt", f"未明確允許{agent}")
    if f"Sitemap: {EXPECTED_BASE}sitemap.xml" not in robots:
        fail(errors, "robots.txt", "Sitemap網址不正確")
    if "Disallow: /" in robots:
        fail(errors, "robots.txt", "不得封鎖全站")

    if errors:
        print("網站驗證失敗：")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "網站驗證通過：7個HTML頁面、唯一title/description、H1、圖片、內部連結、"
        "JSON-LD、集中資料、robots與sitemap均通過檢查。"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
