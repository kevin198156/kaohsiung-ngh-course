# SEO 與 AI 搜尋基準報告

## 基本資料

| 項目 | 基準資料 | 證據分類 |
|---|---|---|
| 網站名稱 | 高雄NGH催眠執行師課程資訊站 | 可確認的事實 |
| 公開網址 | https://kevin198156.github.io/kaohsiung-ngh-course/ | 可確認的事實 |
| 正式課程來源 | https://eec.nuk.edu.tw/course_detail.php?sn=1059 | 可確認的事實 |
| 網站上線日期 | 2026-07-24；GitHub公開部署紀錄最早成功時間為11:55:20（台灣時間） | 可確認的事實 |
| Google索引申請日期 | 2026-07-24；專案紀錄顯示首頁已送出索引申請，帳號內的精確紀錄仍待使用者確認 | 人工觀察／待確認 |
| 本次基準檢查日期 | 2026-07-24（Asia/Taipei） | 可確認的事實 |

## 公開頁面清單

`sitemap.xml`目前列出5個主要頁面。`404.html`是錯誤頁，不列入sitemap。

| 頁面 | 用途 | HTTP狀態 |
|---|---|---:|
| https://kevin198156.github.io/kaohsiung-ngh-course/ | 課程首頁 | 200 |
| https://kevin198156.github.io/kaohsiung-ngh-course/instructor.html | 講師與品牌資料 | 200 |
| https://kevin198156.github.io/kaohsiung-ngh-course/faq.html | 常見問題 | 200 |
| https://kevin198156.github.io/kaohsiung-ngh-course/course-guide.html | 選課比較指南 | 200 |
| https://kevin198156.github.io/kaohsiung-ngh-course/policy.html | 政策、來源與隱私 | 200 |
| https://kevin198156.github.io/kaohsiung-ngh-course/404.html | 自訂404頁面檔案 | 200 |

隨機測試不存在的網址`/not-found-baseline-check-20260724`回傳HTTP 404，並顯示自訂404內容。直接開啟`404.html`本身回傳200，這是GitHub Pages靜態檔案的正常行為。

## SEO技術狀態

### 每頁中繼資料

| 頁面 | title | description | canonical | meta robots | JSON-LD |
|---|---|---|---|---|---|
| 首頁 | 2026高雄NGH催眠執行師課程｜高雄大學100小時實體班 | 已設定且與其他頁不同 | 首頁完整網址 | 未明列；未發現`noindex` | 可解析：Course、EducationEvent、BreadcrumbList |
| 講師頁 | 蔡惠婷老師與睿思品牌｜高雄NGH催眠課程師資資料 | 已設定且與其他頁不同 | `instructor.html`完整網址 | 未明列；未發現`noindex` | 可解析：Person、Organization、BreadcrumbList |
| FAQ | 高雄NGH催眠課程常見問題｜費用、時數、證書與報名 | 已設定且與其他頁不同 | `faq.html`完整網址 | 未明列；未發現`noindex` | 可解析：BreadcrumbList |
| 選課指南 | 高雄催眠課程怎麼選？費用、時數、師資與證書比較指南 | 已設定且與其他頁不同 | `course-guide.html`完整網址 | 未明列；未發現`noindex` | 可解析：Article、BreadcrumbList |
| 政策頁 | 課程政策、資料來源與隱私說明｜高雄NGH課程資訊站 | 已設定且與其他頁不同 | `policy.html`完整網址 | 未明列；未發現`noindex` | 可解析：BreadcrumbList |
| 404頁 | 找不到頁面｜高雄NGH催眠執行師課程資訊站 | 已設定且與其他頁不同 | `404.html`完整網址 | 未明列；未發現`noindex` | 無JSON-LD |

本次只確認JSON-LD是有效JSON、類型可讀取，且自動驗證器未發現錯誤；這不等同Google保證顯示複合式搜尋結果。

### robots.txt

- 公開網址回傳HTTP 200。
- 允許一般爬蟲、Googlebot、Bingbot及OAI-SearchBot。
- 未封鎖全站。
- 已指向正確的`sitemap.xml`。

### sitemap.xml

- 公開網址回傳HTTP 200，Content-Type為`application/xml`。
- 列出5個主要頁面，網址順序與專案驗證器預期一致。
- 各頁`lastmod`均為`2026-07-24`。
- 404頁未列入sitemap。

### 內部連結、圖片與正式報名連結

- `python -X utf8 scripts/validate_site.py`通過：6個HTML頁面的title、description、H1、圖片、內部連結、JSON-LD、集中資料、robots與sitemap均通過。
- 瀏覽器檢查未發現載入失敗的圖片或主控台錯誤。
- 5個主要頁面均保留國立高雄大學正式課程頁連結。
- 正式課程頁於2026-07-24回傳HTTP 200。
- 桌機1440×900與手機390×844檢查均未出現水平溢位；導覽、主要標題、課程摘要與正式報名按鈕可見。

### GitHub Pages發布狀態

- 儲存庫：`kevin198156/kaohsiung-ngh-course`，公開，預設分支為`main`。
- 首次成功GitHub Pages部署：2026-07-24 11:55:20（台灣時間）。
- 本次檢查時最新成功部署：2026-07-24 12:44:06（台灣時間）。
- 最新成功部署commit：`1a2cb665ff8578deb5216878909e085731bd4947`。
- 最新部署網址與本報告記錄的公開網址一致。

### 技術基準結論

2026-07-24本次檢查未發現會明顯阻止公開頁面開啟、爬蟲讀取、內部導覽或前往正式報名頁的技術錯誤。這只代表本次檢查通過，不代表搜尋引擎一定收錄、排名或顯示結構化資料。

## Google與Bing收錄基準

收錄狀態必須以Search Console、Bing Webmaster Tools或明確的逐頁人工檢查為準。本次沒有使用個人化Google搜尋畫面當成排名或收錄證明。

| 頁面 | Google | Bing | 判讀說明 |
|---|---|---|---|
| 首頁 | 待確認；已於2026-07-24送出索引申請 | 已收錄（人工觀察） | 同日專案紀錄記載Bing URL Inspection顯示「Indexed successfully」；Google實際網址測試只證明可抓取與允許索引，不證明已收錄 |
| 講師頁 | 待確認 | 待確認 | Sitemap發現網址不等同完成收錄 |
| FAQ | 待確認 | 待確認 | Sitemap發現網址不等同完成收錄 |
| 選課指南 | 待確認 | 待確認 | Sitemap發現網址不等同完成收錄 |
| 政策頁 | 待確認 | 待確認 | Sitemap發現網址不等同完成收錄 |

已知帳號內紀錄：

- Google Search Console網址前綴資源已驗證，sitemap已提交，首頁可抓取且允許建立索引。
- Bing Webmaster Tools已由Google Search Console匯入；sitemap曾顯示發現5個網址、0個錯誤、0個警告。
- 上述紀錄不代表5頁都已收錄，也不代表任何排名。

## 已知外部連結

### 指向本站的連結

- GitHub儲存庫README包含公開網站網址；這是專案自有頁面，不算第三方推薦。
- 2026-07-24以完整公開網址進行一般網路搜尋，未找到可可靠確認的第三方反向連結。搜尋結果可能不完整，因此只能記為「目前未確認」，不能宣稱完全沒有外部連結。

### 本站連出的主要外部來源

- 國立高雄大學推廣教育中心正式課程頁。
- 國立高雄大學交通資訊。
- 睿思公開Facebook頁面。
- GitHub隱私權聲明。

## 目前限制與尚未取得的數據

- 尚未取得Search Console的點擊、曝光、CTR、平均排名、查詢字詞與頁面資料。
- 尚未在Search Console逐頁確認5個主要頁面的Google索引狀態。
- Bing只有首頁的同日人工觀察紀錄，其餘4頁尚未逐頁確認。
- 尚未執行8組固定關鍵字的無痕人工排名觀察。
- 尚未執行ChatGPT、Gemini、Microsoft Copilot及Perplexity的固定問題測試。
- 尚無28天或90天趨勢，不能做上線前後成效歸因。
- 反向連結搜尋不是完整的專業外鏈資料庫，不能據此宣稱外鏈總數。
- 本次沒有大量或自動抓取Google搜尋結果，也沒有把個人化搜尋畫面當成客觀排名。
- Search Console屬登入後資料，本次無法直接讀取，因此沒有填入任何推測數字。

## 檢查日期、方法與來源

| 日期 | 檢查項目 | 方法 | 來源 |
|---|---|---|---|
| 2026-07-24 | 頁面、robots、sitemap、CSS、404、正式課程頁HTTP回應 | PowerShell HTTP HEAD/GET檢查 | 公開網站與國立高雄大學正式課程頁 |
| 2026-07-24 | title、description、canonical、meta robots、JSON-LD、圖片、瀏覽器錯誤 | 瀏覽器DOM與主控台檢查 | 公開網站 |
| 2026-07-24 | 桌機與手機顯示 | 1440×900及390×844實際瀏覽檢查 | 公開首頁 |
| 2026-07-24 | 內部連結、圖片、H1、集中資料、robots、sitemap | `python -X utf8 scripts/validate_site.py` | 目前儲存庫 |
| 2026-07-24 | 上線與最新部署狀態 | GitHub公開Deployments API | GitHub儲存庫 |
| 2026-07-24 | Google與Bing既有設定紀錄 | 閱讀`TEST_REPORT.md`與`MANUAL_SETUP_GUIDE.md` | 目前儲存庫 |
| 2026-07-24 | 正式課程來源仍可開啟 | 公開頁面與HTTP檢查 | 國立高雄大學推廣教育中心 |
| 2026-07-24 | 已知反向連結 | 以完整網址進行一次一般網路搜尋 | 公開網路搜尋；非完整外鏈資料庫 |
