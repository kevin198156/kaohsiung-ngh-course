# 網站上線與搜尋引擎手動設定指南

這份指南只列出必須由專案負責人登入或確認的步驟。請勿把GitHub、Google、Microsoft或其他帳號密碼貼給Codex。

## 已完成：GitHub與網站發布

Codex已完成以下工作，不需要再操作GitHub驗證碼：

- GitHub CLI已登入帳號`kevin198156`。
- 已建立公開儲存庫`kaohsiung-ngh-course`。
- 已把網站推送到`main`分支。
- GitHub Pages已設定從`main`分支的`/(root)`資料夾發布。
- 公開網址、頁面、圖片、robots、sitemap、手機版及404回應均已檢查。

公開網址：

`https://kevin198156.github.io/kaohsiung-ngh-course/`

## 已完成：Google Search Console

2026年7月24日完成：

- 已用首頁HTML標記驗證網站擁有權。
- 已成功提交`sitemap.xml`。
- 實際網址測試確認Google可抓取首頁，且允許建立索引。
- 已送出首頁建立索引要求。

以下步驟保留作為日後重新設定時的操作紀錄。

### 1. 新增網站資源

1. 進入`https://search.google.com/search-console/`並登入Google帳號。
2. 點左上角的資源選單，再點「新增資源」。
3. 選右側「網址前置字元」。
4. 貼上完整網址：

   `https://kevin198156.github.io/kaohsiung-ngh-course/`

5. 點「繼續」。

### 2. 選擇驗證方式

GitHub Pages專案網站建議選「HTML標記」，因為不需要更改DNS。

1. 展開「HTML標記」。
2. 複製完整的`<meta name="google-site-verification" ...>`標記。
3. 先不要按「驗證」。
4. 只把完整meta標記貼回Codex，不要提供Google帳號或密碼。
5. Codex會把標記加入首頁、提交並重新發布。
6. Codex通知完成後，回到Search Console點「驗證」。
7. 完成後回覆Codex：「Google驗證成功」。

### 3. 提交sitemap

1. 在Search Console左側點「Sitemap」。
2. 在網址後方欄位輸入`sitemap.xml`。
3. 點「提交」。
4. 完整網站地圖網址應為：

   `https://kevin198156.github.io/kaohsiung-ngh-course/sitemap.xml`

### 4. 檢查首頁並申請建立索引

1. 在上方「檢查任何網址」貼上首頁完整網址。
2. 等待檢查完成。
3. 如果顯示尚未建立索引，點「要求建立索引」。
4. 幾天後回來確認Google是否已發現或收錄。

建立索引可能需要時間；提交不代表保證收錄或排名。

## 已完成：Bing Webmaster Tools

2026年7月24日完成：

- 已從Google Search Console匯入並自動驗證網站。
- Sitemap狀態為成功，發現5個網址，0個錯誤、0個警告。
- URL Inspection顯示首頁「Indexed successfully」，可出現在Bing。

以下步驟保留作為日後重新設定時的操作紀錄。

### 建議方式：從Google Search Console匯入

1. 進入`https://www.bing.com/webmasters/`並登入Microsoft帳號。
2. 選「Import」或「從Google Search Console匯入」。
3. 授權讀取剛才建立的Google Search Console資源。
4. 選取本網站並完成匯入。
5. 到「Sitemaps」確認或提交：

   `https://kevin198156.github.io/kaohsiung-ngh-course/sitemap.xml`

6. 使用「URL Inspection」檢查首頁能否抓取。

### 如果不從Google匯入

1. 選「Add a site」並貼上首頁完整網址。
2. 選「HTML Meta Tag」驗證。
3. 複製完整的Bing驗證meta標記。
4. 先不要按驗證，把完整meta標記貼回Codex。
5. Codex加入、提交並發布後，再回Bing按「Verify」。

### IndexNow

目前Bing已成功讀取sitemap並索引首頁，因此不需要為這個低頻更新的網站增加IndexNow流程。若日後更新頻繁，再請Codex評估建立IndexNow金鑰檔與提交流程；不要把任何帳號密碼交給Codex。

## 搜尋引擎設定後：真實外部平台待辦

只在您有管理權限、內容真實且平台規範允許的頁面加入連結。

- [ ] Google商家檔案：只有睿思實際符合商家資格時，才在商家資訊或貼文加入活動頁／正式課程頁。不要把高雄大學地址設為睿思營業地址。
- [ ] 睿思Facebook粉絲頁：發布課程摘要，清楚標示正式招生以高雄大學公告為準，加入正式課程頁。
- [ ] Instagram：在個人檔案或相關貼文加入活動頁；不要承諾排名、證書核發或療效。
- [ ] YouTube：在相關影片資訊欄加入活動頁與正式課程頁。
- [ ] LINE官方帳號：建立包含日期、費用、正式報名連結的圖文訊息。
- [ ] 講師公開介紹頁：加入高雄大學正式課程連結及本活動資訊頁。
- [ ] 其他真實合作單位：只有取得對方同意且合作關係可證明時才加入。

所有外部文案都應保留：「正式招生、繳費、退費、開課與課程異動，以國立高雄大學推廣教育中心最新公告為準。」

## 重要限制

網站上線、提交索引及結構化資料，只能增加被發現和理解的機會，不能保證搜尋排名、AI引用或推薦。
