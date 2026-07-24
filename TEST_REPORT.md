# 網站測試報告

測試日期：2026年7月24日

公開網址：https://kevin198156.github.io/kaohsiung-ngh-course/

測試版本：GitHub `main` 分支，提交 `b6d52a1`

## 自動化檢查

執行：

```text
python -X utf8 scripts/validate_site.py
```

結果：通過。

檢查範圍包括：

- 6個HTML頁面均可解析，且分別具有唯一的 `title` 與 `meta description`。
- 每頁均有且只有一個主要H1，並設定 `lang="zh-Hant-TW"`。
- canonical、Open Graph、內部連結、圖片路徑及圖片尺寸設定完整。
- 圖片具有適當替代文字；純裝飾圖片使用空白 `alt`。
- 所有JSON-LD均可解析，且未加入評論、評分或未確認優惠。
- `content/course-data.json` 可解析，必填資料與待補資料分開保存。
- `robots.txt` 未封鎖Googlebot、Bingbot或OAI-SearchBot。
- `sitemap.xml` 列出5個主要頁面，網址與最後更新日期格式正確。
- 全站未發現 `noindex`、混合內容或付費服務依賴。

## 公開網站檢查

- 首頁、講師頁、FAQ、選課指南、政策頁、`404.html`、`robots.txt`、`sitemap.xml` 與CSS均回傳HTTP 200。
- 不存在的測試網址回傳HTTP 404，GitHub Pages會顯示自訂404內容。
- 講師照片、品牌圖與社群分享圖均回傳HTTP 200。
- 正式課程頁、高雄大學交通資訊、睿思Facebook頁及GitHub隱私聲明均回傳HTTP 200。
- GitHub Pages最新建置狀態為 `built`，對應提交 `b6d52a1`。

## HTML標準與結構化資料

- 6個公開HTML頁面均通過W3C Nu HTML Validator：0 errors、0 warnings。
- 自動化檢查已逐段解析所有JSON-LD。
- JSON-LD可見資料與頁面文字一致，未建立虛構評論、評分、成效或醫療效果。
- Google Rich Results Test與Schema.org Validator仍建議在搜尋引擎開始抓取後人工複查；不同Schema類型不一定會顯示為Google複合式搜尋結果。

## 手機與桌機

以公開網站實測：

- 手機寬度360至375px：6個頁面均無整頁橫向溢出。
- 費用與比較表在自身容器內可橫向捲動，不會撐寬頁面。
- 桌機寬度1265px：首頁無橫向溢出。
- 導覽列、主要按鈕、焦點樣式與內容區塊可正常顯示。
- 圖片均成功載入，瀏覽器主控台未見明顯JavaScript錯誤。
- 網站未使用JavaScript，因此沒有前端腳本執行或第三方腳本阻塞問題。

## 效能與可及性

- 網站採純HTML與CSS，沒有框架、追蹤碼、外部字型或第三方JavaScript。
- 三張本機圖片合計約279KB，其餘頁面與CSS體積小。
- 設有跳至主要內容連結、鍵盤焦點樣式及 `prefers-reduced-motion`。
- 主要文字與按鈕配色經靜態對比檢查，達一般文字WCAG AA對比需求。
- Google PageSpeed Insights API於測試時回傳HTTP 429流量限制，因此本次未取得可重現的Lighthouse分數；不以未執行的分數宣稱通過。

## 內容與風險檢查

- 日期、費用、時數、證書費、出席與個案條件均以國立高雄大學公開課程頁為主要來源。
- 已清楚區分國立高雄大學正式招生、蔡惠婷老師授課及睿思推廣角色。
- 已標示課程為推廣教育與技能培訓，不等同醫師、心理師或台灣法定醫事證照。
- 未宣稱治療、治癒、保證改善疾病、保證排名、保證收錄或保證AI推薦。
- 網站不設報名表單，不收集姓名、身分證、付款或健康資料。

## 尚需上線後人工完成

- Google Search Console新增網址前綴資源、驗證網站、提交 `sitemap.xml` 及申請首頁建立索引。
- Bing Webmaster Tools新增網站、驗證、提交 `sitemap.xml` 並檢查抓取狀態。
- 以Google Rich Results Test及Schema.org Validator人工檢視公開首頁。
- 依 `SEARCH_TEST_PLAN.md` 定期記錄Google、Bing、ChatGPT搜尋、Gemini、Copilot與Perplexity的實際發現及引用狀況。

網站上線、提交索引及結構化資料，只能增加被發現和理解的機會，不能保證搜尋排名、AI引用或推薦。
