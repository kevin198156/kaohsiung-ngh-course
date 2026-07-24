# 網站上線與搜尋引擎手動設定指南

這份指南只列出必須由專案負責人登入或確認的步驟。請勿把GitHub、Google、Microsoft或其他帳號密碼貼給Codex。

## 第一階段：重新登入GitHub，讓Codex建立儲存庫

目前電腦上的GitHub登入已失效，但網站檔案不受影響。

1. 由Codex啟動GitHub重新登入後，瀏覽器會顯示GitHub授權頁。
2. 確認登入的帳號是`kevin198156`。
3. 只核准GitHub官方命令列工具要求的存取。
4. 完成後回覆Codex：「GitHub授權完成」。
5. Codex接著會：
   - 建立名為`kaohsiung-ngh-course`的公開儲存庫；
   - 上傳已測試的網站；
   - 啟用或帶您啟用GitHub Pages；
   - 確認公開網址、robots、sitemap與手機版。

不要先建立不同名稱的儲存庫，因為網站內的正式網址已依`kaohsiung-ngh-course`設定。若一定要使用其他名稱，先告訴Codex同步更改全站網址。

## 第二階段：確認GitHub Pages

如果Codex無法代為啟用，請依下列步驟操作：

1. 進入`https://github.com/kevin198156/kaohsiung-ngh-course`。
2. 點上方「Settings」。
3. 左側點「Pages」。
4. 在「Build and deployment」的「Source」選「Deploy from a branch」。
5. 「Branch」選`main`，資料夾選`/(root)`。
6. 點「Save」。
7. 等待約數分鐘，重新整理同一頁。
8. 看到公開網址後，回覆Codex：「Pages已啟用，網址是……」。
9. Codex會檢查實際公開網站、所有連結、robots.txt、sitemap.xml及行動版。

預定公開網址：

`https://kevin198156.github.io/kaohsiung-ngh-course/`

## 第三階段：Google Search Console

請等GitHub Pages公開網址可正常開啟後再進行。

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

## 第四階段：Bing Webmaster Tools

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

IndexNow不是本網站上線的必要條件。若Bing已能讀取sitemap，可先使用Bing的網址提交功能。若日後更新頻繁，再請Codex建立IndexNow金鑰檔與提交流程；不要把任何帳號密碼交給Codex。

## 第五階段：真實外部平台待辦

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

