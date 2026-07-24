# 高雄NGH課程YouTube Shorts

這是以官方開源HyperFrames v0.7.70製作的25.5秒繁體中文直式宣傳片專案。
影片採本機HTML-to-video渲染，不使用雲端算圖、API金鑰、旁白、音樂或音效。

## 主要交付

- `output/kaohsiung-ngh-course-youtube-short.mp4`
- `subtitles/kaohsiung-ngh-course-zh-Hant.srt`
- `thumbnails/youtube-thumbnail-1280x720.jpg`
- `thumbnails/youtube-short-cover-1080x1920.jpg`
- `YOUTUBE_UPLOAD_COPY.md`
- `YOUTUBE_UPLOAD_CHECKLIST.md`
- `VIDEO_QA_REPORT.md`

## 來源

- 國立高雄大學正式課程頁：https://eec.nuk.edu.tw/course_detail.php?sn=1059
- 活動資訊站：https://kevin198156.github.io/kaohsiung-ngh-course/
- HyperFrames官方專案：https://github.com/heygen-com/hyperframes
- 固定版本：v0.7.70

## 本機重製

需求：Node.js 22以上、FFmpeg 6以上、ffprobe、HyperFrames官方Chrome Headless Shell。

```text
npm.cmd install
npm.cmd run check
npm.cmd run render
```

最終MP4及暫存檔依儲存庫 `.gitignore` 排除，不提交Git。來源、字幕、縮圖與QA文件可提交。

## 技術結構

- `index.html`：1080×1920、25.5秒、30fps的主組合。
- `src/styles.css`：網站品牌配色、Shorts安全區及直式排版。
- `src/animation.js`：單一暫停GSAP時間軸與有限動畫。
- `frame.md`：影片視覺規格。
- `BRIEF.md`、`SCRIPT.md`、`STORYBOARD.md`：製作決策、腳本及分鏡。
- `src/thumbnail-*.html`：縮圖與Shorts封面可重製來源。

## 內容界線

正式招生、繳費、退費、開課與課程異動，以國立高雄大學推廣教育中心最新公告為準。
本課程屬推廣教育與技能培訓，不等同醫師、心理師或台灣法定醫事專業執照，也不取代醫療診斷或心理治療。
