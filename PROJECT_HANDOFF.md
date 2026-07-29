# 專案交接：高雄 NGH 催眠執行師課程資訊站

> 未來任何新 Codex Session 或維護者進入本專案時，請依序閱讀 `AGENTS.md`、`PROJECT_HANDOFF.md`、`README.md` 與 `content/course-data.json`。

## 1. 專案目的

本站整理 2026 年國立高雄大學推廣教育中心「美國 NGH 催眠執行師國際證照授證課程（實體課）」的公開資訊，協助搜尋引擎與一般使用者理解課程，並導向正式課程頁完成報名。

- 正式課程、招生、繳費、退費、開課與異動來源：[國立高雄大學推廣教育中心課程頁](https://eec.nuk.edu.tw/course_detail.php?sn=1059)
- GitHub Pages 公開網址：[https://kevin198156.github.io/kaohsiung-ngh-course/](https://kevin198156.github.io/kaohsiung-ngh-course/)
- 本站是課程推廣與資訊整理頁，不是正式報名後台；本站不收集姓名、身分證字號、電話、地址或其他報名個資。

## 2. 技術架構

- 網站為純 HTML5 與 CSS 靜態網站；頁面中的 JSON-LD 為結構化資料，沒有網站執行所需的前端 JavaScript 或建置流程。
- CSS 共用檔為 `assets/styles.css`；圖片放在 `assets/images/`。
- GitHub Pages 目前以 legacy Pages 模式，從 `main` 分支的儲存庫根目錄（`/`）發布；不要更改這項設定。
- 根目錄沒有網站建置指令、套件管理檔或 GitHub Actions 部署工作流程。`video/hyperframes-course-promo/` 是獨立的短影音來源，不參與網站發布。
- 本機預覽可在根目錄執行：

```powershell
python -m http.server 8765 --bind 127.0.0.1
```

  然後開啟 `http://127.0.0.1:8765/`；以 `Ctrl+C` 停止。

- 網站驗證：

```powershell
python -X utf8 scripts/validate_site.py
```

## 3. 重要檔案地圖

| 檔案／資料夾 | 用途 |
|---|---|
| `index.html` | 課程首頁、費用／日期摘要、催眠簡介、報名入口；含 Course、EducationEvent 與 BreadcrumbList JSON-LD。 |
| `instructor.html` | 蔡惠婷老師、品牌角色與來源界線；含 Person、Organization 與 BreadcrumbList JSON-LD。 |
| `faq.html` | 常見問題、補課、費用、證書與正式報名說明。 |
| `course-guide.html` | 客觀的高雄催眠課程選擇指南；快速選課重點與原生 `<details>` 進階內容。 |
| `registration-guide.html` | 高雄大學會員註冊、登入與正式報名操作指引；本站不受理報名。 |
| `policy.html` | 網站角色、資料來源、退費摘要、隱私、外部連結與健康／專業界線。 |
| `404.html` | 找不到頁面時的導覽入口。 |
| `assets/styles.css` | 全站共用樣式、響應式導覽、卡片與按鈕。 |
| `assets/images/` | 已使用的講師、Logo 與社群分享圖片素材。 |
| `content/course-data.json` | 集中課程資料、資料來源、講師提供資料與待補項目；不是自動產生 HTML 的資料源。 |
| `llms.txt` | 提供搜尋型 AI 參考的公開摘要；不是收錄、引用或推薦的保證。 |
| `sitemap.xml` | 六個主要公開頁面的網址與 `lastmod`。 |
| `robots.txt` | 明確允許 Googlebot、Bingbot、OAI-SearchBot，並指定 sitemap。 |
| `scripts/validate_site.py` | 以 Python 標準函式庫檢查七個 HTML 頁面、SEO 基本項、連結、JSON-LD、集中資料、robots 與 sitemap。 |
| `AGENTS.md` | 專案不可違反的維護規則。 |
| `README.md` | 人類快速導覽、公開網址與一般維護說明。 |
| `SEARCH_TEST_PLAN.md` | 上線後 Google、Bing 與搜尋型 AI 的人工測試計畫。 |
| `tracking/CHANGE_LOG.md` | 已完成網站、SEO 與追蹤變更紀錄。 |
| `tracking/` | 基準報告、關鍵字、AI 能見度、Search Console 與 28 天成效追蹤資料。 |
| `MANUAL_SETUP_GUIDE.md` | GitHub Pages、Google Search Console 與 Bing Webmaster Tools 的人工設定指南。 |
| `video/hyperframes-course-promo/` | 獨立的 HyperFrames YouTube Shorts 專案與上傳素材，不影響網站靜態發布。 |

## 4. 資料來源與同步關係

### 資料來源原則

- 課程日期、時數、費用、優惠、報名、退費、結業與證書，以高雄大學正式課程頁優先。
- `content/course-data.json` 集中記錄課號、日期、時數、地點、費用、證書費、講師、主辦單位、報名網址、聯絡資料、來源與待補項目。
- 講師提供資料、教材／餐費等未由高雄大學逐項列示的資訊，必須保留來源界線；不可寫成高雄大學官方列示資料。
- 現有 HTML 是直接維護，不會由 JSON 自動產生。只更新 JSON 不會更新可見網頁、meta、JSON-LD 或 `llms.txt`。

### 目前常見的直接寫入位置

費用、時數、教材／餐費、補課與講師資料會出現在 `index.html`、`faq.html`、`course-guide.html`、`instructor.html`、`policy.html` 與 `llms.txt` 的不同組合。報名註冊／登入網址另出現在 `registration-guide.html`。每次先用 `rg` 搜尋舊值與相關關鍵字，確認實際受影響頁面後再改。

### 資料變更同步檢查表

| 變更類型 | 至少同步檢查 |
|---|---|
| 日期、時間、時數、地點或課號 | `content/course-data.json`、`index.html`、`faq.html`、`course-guide.html`、相關 JSON-LD、`llms.txt`、各受影響頁的最後更新日期、`sitemap.xml` 的 `lastmod`、`tracking/CHANGE_LOG.md`。 |
| 學費、優惠、教材／餐費或 NGH 證書費 | `content/course-data.json`、`index.html`、`faq.html`、`course-guide.html`、`policy.html`、含 Offer 的 JSON-LD、`llms.txt`、最後更新日期、`sitemap.xml`、`tracking/CHANGE_LOG.md`。 |
| 講師姓名、資格或品牌角色 | `content/course-data.json`、`index.html`、`instructor.html`、`course-guide.html`、必要的 FAQ／政策文字、Person／Course／Event JSON-LD、`llms.txt`、最後更新日期、`sitemap.xml`、`tracking/CHANGE_LOG.md`。 |
| 補課、出席、考核、證書、退費或報名網址 | `content/course-data.json`、首頁、FAQ、選課指南、報名指南或政策頁、相關 JSON-LD、`llms.txt`、最後更新日期、`sitemap.xml`、`tracking/CHANGE_LOG.md`。 |
| 新增公開頁面 | 新頁本身的 `lang`、唯一 title／description、canonical、Open Graph、JSON-LD、麵包屑、H1、最後更新日期與正式課程連結；全部頁面的導覽與適用頁尾、`404.html` 導覽、`sitemap.xml`、`llms.txt`、`README.md`、`scripts/validate_site.py` 的頁面與 sitemap 預期清單、`tracking/CHANGE_LOG.md`。 |

可見內容、JSON-LD、`llms.txt`、`sitemap.xml` 與最後更新日期必須相互一致；任何來源資料不足時，先更新 `pendingData`，不要把待補文字發布到 HTML。

## 5. 不可破壞的規則

- 正式招生、繳費、退費及課程異動以高雄大學公告為準。
- 不得杜撰講師學歷、證照、經歷、評價、成效、優惠、合作關係或排名。
- 不得保證醫療、心理治療、治癒、疾病改善或特定身心效果。
- 「樹德科技大學人類性學研究所博士生」必須保留「博士生」身分與講師提供資料界線，不得寫成已取得博士學位。
- 本站不得自行收集報名個資，亦不得以本站取代高雄大學註冊、登入、報名或繳費流程。
- 不得移除高雄大學正式報名連結、資料來源聲明、隱私說明與健康／專業免責內容。
- 不得任意變更 canonical 網域、GitHub Pages 發布來源、網域、`robots.txt` 的允許規則或 sitemap 基底網址。
- 不得加入 `noindex`，也不得封鎖 Googlebot、Bingbot 或 OAI-SearchBot。

## 6. 標準修改流程

1. 依序閱讀 `AGENTS.md`、`PROJECT_HANDOFF.md`、`README.md` 與 `content/course-data.json`。
2. 確認專案路徑、目前 Git 分支、`git status`、未追蹤檔案與最近 commit。
3. 保護未追蹤及不屬於本次任務的檔案；目前已知 `Codex製作本頁說明.txt` 必須保持未追蹤，除非專案負責人明確另行指示。
4. 在確認需求後建立功能分支；不要直接在 `main` 修改。
5. 先由高雄大學正式頁核對核心資料，再更新集中資料與所有受影響的可見內容、JSON-LD、SEO 檔案。
6. 執行自動驗證與必要的文字搜尋；檢查手機／桌機可讀性與外部報名流程。
7. 以 `git diff` 與 `git diff --check` 檢查範圍及格式，確認沒有夾帶不屬於任務的檔案。
8. 取得確認後建立清楚的小型 commit。
9. 經人工或獨立模型驗收後，才以一般合併方式合併至 `main`。
10. 只有取得明確授權時才推送、部署；部署後確認公開網站、robots、sitemap 與新增頁面。

## 7. 驗證與測試

```powershell
# 執行靜態網站檢查
python -X utf8 scripts/validate_site.py

# 檢查未提交變更的空白與衝突標記問題
git diff --check

# 在功能分支比較 main 與目前分支的格式問題
git diff --check main...HEAD

# 依實際需求搜尋舊資料或高風險文字
rg -n "舊日期|舊金額|舊資格" .
```

驗證器會檢查：公開 HTML 是否存在、唯一 title／description、單一 H1、canonical、圖片 alt／尺寸、內部連結、JSON-LD 是否可解析、集中資料基本網址、robots 與 sitemap。

仍需人工確認的事項：

- 窄螢幕的實際視覺、導覽列、按鈕與卡片沒有擠壓或水平溢出。
- 高雄大學外部註冊、登入、正式課程頁仍可開啟，且操作流程沒有改版。
- 新增或變更的資訊確實已獲專案負責人確認，且來源界線正確。
- 合併／推送後，GitHub Pages 實際顯示為已完成，公開網址回應新版本。
- Search Console、Bing 與 AI 測試須依 `SEARCH_TEST_PLAN.md` 與 `tracking/` 人工記錄，不能以預估數字取代。

## 8. 已知限制與技術債

- 手機版固定頁首在窄螢幕上偏高，但目前未影響導覽與功能；若未來調整，須以實機／瀏覽器寬度測試為準。
- `content/course-data.json` 不會自動產生全部 HTML，仍有人工同步需求。
- 搜尋引擎索引、排名與搜尋型 AI 的引用／推薦皆不能保證。
- 高雄大學外部課程頁、會員系統與報名流程可能日後變更，更新前必須重新核對。
- 講師提供資料中仍有未附公開查證網址的項目；不得將其擴寫成官方可驗證事實。

## 9. 最近一次重要變更

2026-07-29 完成第二階段內容調整：

- 更新講師資格呈現與來源界線。
- 補充教材包含、餐費不包含及 NGH 證書費另計。
- 調整補課規則為須與講師協調、依實際可行性確認。
- 在首頁增加安全的催眠簡介。
- 將選課指南前段改為快速重點，進階內容使用原生 `<details>`。
- 新增高雄大學會員註冊與正式報名操作指南。

相關 commit：

- `1956fb1 Update course content and registration guide`
- `9700a07 Fix structured data and review findings`

完整歷程請閱讀 `tracking/CHANGE_LOG.md`。

## 新 Codex Session 啟動提示詞

```text
請先閱讀本專案根目錄的 AGENTS.md、PROJECT_HANDOFF.md、README.md 與 content/course-data.json。接著檢查目前 Git 分支、工作區、未追蹤檔案及網站驗證方式。現在只進行盤點，不修改任何檔案。請回報專案架構、與本次需求相關的檔案、資料同步風險、預計修改計畫與測試，等我確認後再開始。
```