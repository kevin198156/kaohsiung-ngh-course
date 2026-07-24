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

## 主要資料來源

- 正式課程頁：https://eec.nuk.edu.tw/course_detail.php?sn=1059
- 高雄大學交通資訊：https://www.nuk.edu.tw/p/412-1000-587.php?Lang=zh-tw
- 集中資料檔：`content/course-data.json`

## 發布方式

- GitHub Pages從`main`分支的儲存庫根目錄發布。
- 預定公開網址：`https://kevin198156.github.io/kaohsiung-ngh-course/`
- 儲存庫名稱若改變，必須全站搜尋並更新`kaohsiung-ngh-course`與所有canonical、Open Graph、JSON-LD、robots、sitemap及llms網址。

