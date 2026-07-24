# 高雄NGH催眠執行師課程資訊站

繁體中文、手機優先、零建置工具的GitHub Pages靜態網站，用於整理2026年國立高雄大學推廣教育中心「美國NGH催眠執行師國際證照授證課程」公開資訊，並將使用者導向正式課程頁報名。

## 預定公開網址

https://kevin198156.github.io/kaohsiung-ngh-course/

## 網站頁面

- `index.html`：課程首頁
- `instructor.html`：講師與品牌
- `faq.html`：常見問題
- `course-guide.html`：高雄催眠課程選擇指南
- `policy.html`：政策、來源、隱私與專業界線
- `404.html`：找不到頁面

## 資料與搜尋檔案

- `content/course-data.json`：集中課程資料、來源與待確認項目
- `robots.txt`：允許一般搜尋引擎、Googlebot、Bingbot與OAI-SearchBot
- `sitemap.xml`：五個主要頁面的網站地圖
- `llms.txt`：給搜尋型AI參考的補充摘要；不是收錄必要條件
- `MANUAL_SETUP_GUIDE.md`：GitHub Pages、Google與Bing手動設定指南
- `SEARCH_TEST_PLAN.md`：上線後搜尋與AI查詢紀錄方式
- `TEST_REPORT.md`：自動檢查結果與上線後待補測項目
- `COURSE_WEBSITE_MASTER_PROMPT.md`：新課程可重複使用的完整Codex建站、SEO、部署與追蹤母提示詞

## 長期SEO與AI搜尋追蹤

`tracking/`是本專案正式交付的一部分：

- `BASELINE_REPORT.md`：上線技術、部署、索引與資料缺口基準
- `KEYWORD_TRACKING.csv`：Google與Bing固定關鍵字人工觀察
- `AI_VISIBILITY_TRACKING.csv`：ChatGPT、Gemini、Copilot與Perplexity能見度紀錄
- `SEARCH_CONSOLE_DATA.csv`：Search Console實際匯出資料整理表
- `CHANGE_LOG.md`：網站、SEO與追蹤變更紀錄
- `REPORT_28_DAYS_TEMPLATE.md`：上線28天成效報告模板
- `TRACKING_GUIDE.md`：第7、28、90天檢查、匯出與證據保存指南

追蹤資料必須區分可確認事實、人工觀察、主觀推估與尚無數據支持的假設。不得將高雄大學官方頁的既有排名、流量或報名量計為本站成果。

## 日後更新日期或價格

1. 先查看[國立高雄大學正式課程頁](https://eec.nuk.edu.tw/course_detail.php?sn=1059)。
2. 將新資料與來源交給Codex，指定「依`AGENTS.md`同步更新全站」。
3. Codex會先改`content/course-data.json`，再同步HTML、JSON-LD、sitemap、llms與最後更新日期。
4. 完整測試通過後再提交與發布。

請勿只修改單一頁面上的金額或日期，否則可見內容與搜尋資料可能不一致。

## 本機檢查

```text
python scripts/validate_site.py
```

網站不需要Node.js、資料庫、付費字型、付費圖片或付費主機。

## 重要聲明

本網站不是國立高雄大學官方網站。本頁為課程推廣與資訊整理頁。正式招生、繳費、退費、開課與課程異動規定，均以國立高雄大學推廣教育中心最新公告為準。

本課程屬推廣教育與技能培訓，不等同醫師、心理師或其他台灣法定醫事專業執照，也不取代醫療診斷或心理治療。
