# 網站維護規則

本儲存庫是「高雄NGH催眠執行師課程資訊站」的GitHub Pages靜態網站。所有對外文字使用台灣繁體中文。

## 必須遵守

1. 所有日期、價格、地點、時數、優惠、報名、退費、結業及證書條件，均以國立高雄大學推廣教育中心正式課程頁為優先資料來源。
2. 更新課程資料時，必須同步更新：
   - `content/course-data.json`
   - 所有受影響的HTML可見內容
   - HTML中的JSON-LD
   - `sitemap.xml`的`lastmod`
   - 每頁顯示的最後更新日期
   - `llms.txt`
3. 不得杜撰或暗示未經可靠來源證實的評價、學員人數、資格、經歷、成效、優惠、排名、合作關係、地址、電話或課後支援。
4. 不得加入醫療、心理治療、治癒、疾病改善或特定身心效果保證。
5. 每次變更後必須執行 `python scripts/validate_site.py`，並於可用環境進行手機與桌機瀏覽檢查。
6. 不得刪除來源聲明、健康與專業界線、隱私說明，或國立高雄大學正式報名連結。
7. 不得在本站新增蒐集敏感個資的報名表；正式報名一律導向高雄大學正式課程頁。
8. 不得加入`noindex`，也不得在`robots.txt`封鎖Googlebot、Bingbot或OAI-SearchBot。
9. 結構化資料必須與同一頁可見文字一致，不得放入隱藏優惠、評論、評分或未證實資料。
10. 若正式資料缺少，請在`content/course-data.json`的`pendingData`保留待補項目；不要把`【待提供】`文字發布在對外HTML。
11. 任何title、description、可見文案、JSON-LD、課程日期與條件、外部連結、網站架構、robots或sitemap變更，都必須同步更新`tracking/CHANGE_LOG.md`。
12. 排名、索引、Search Console與AI能見度只能依實際證據記錄；不得杜撰數字，也不得把高雄大學官方頁既有成效算成本站成果。
13. `tracking/`不得存放或提交帳號密碼、OAuth權杖、API金鑰、未遮蔽後台截圖或其他敏感資料。

## 長期成效追蹤

- `tracking/BASELINE_REPORT.md`是上線技術與索引基準。
- `tracking/KEYWORD_TRACKING.csv`分開記錄正式課程頁與GitHub活動頁的人工搜尋位置。
- `tracking/AI_VISIBILITY_TRACKING.csv`記錄ChatGPT、Gemini、Copilot與Perplexity的提及、引用及事實正確性。
- `tracking/SEARCH_CONSOLE_DATA.csv`只填入Search Console實際匯出資料，不得估算。
- `tracking/REPORT_28_DAYS_TEMPLATE.md`用於第一期成效報告。
- `tracking/TRACKING_GUIDE.md`定義第7、28、90天檢查方式、證據保存及不可宣稱事項。

## 主要資料來源

- 正式課程頁：https://eec.nuk.edu.tw/course_detail.php?sn=1059
- 高雄大學交通資訊：https://www.nuk.edu.tw/p/412-1000-587.php?Lang=zh-tw
- 集中資料檔：`content/course-data.json`

## 發布方式

- GitHub Pages從`main`分支的儲存庫根目錄發布。
- 目前公開網址：`https://kevin198156.github.io/kaohsiung-ngh-course/`
- 儲存庫名稱若改變，必須全站搜尋並更新`kaohsiung-ngh-course`與所有canonical、Open Graph、JSON-LD、robots、sitemap及llms網址。
## 交接與 Git 安全程序

- 新 Session 開始時，先依序閱讀本檔案、`PROJECT_HANDOFF.md`、`README.md`與`content/course-data.json`，再進行任何修改。
- 修改前必須檢查目前分支、`git status`、未追蹤檔案與最近 commit；不屬於本次任務的檔案不得暫存、提交、合併或推送。
- 新增公開頁面時，必須同步檢查全站導覽與適用頁尾、`404.html`導覽、canonical、Open Graph、麵包屑、JSON-LD、`sitemap.xml`、`llms.txt`、最後更新日期與`scripts/validate_site.py`。
- 修改完成後，除既有網站驗證外，必須執行`git diff --check`；功能分支可再執行`git diff --check main...HEAD`。
- 未經專案負責人確認，不得直接推送、合併或部署；不得以 force push、rebase、amend 或重寫既有 commit 取代一般安全流程。
