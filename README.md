回傳使用者的匯率資料由即匯站提供，資料的可靠度極高。
採用LINE BOT做為基本架構，結合Python flask套件以及網路爬蟲概念，讓使用者傳送訊息至LINE BOT帳號，帳號接收訊息後再把訊息POST到Webhook URL， Webhook URL就是本人所寫的Web service，負責實際處理收到的訊息。
程式碼中利用到網路爬蟲的語法，從參考網站爬蟲，能夠快速統整數量龐大且複雜的資料中，並從中快速抓取相對對應的匯率，讓使用者快速得到匯率查詢結果。

三折頁:
![投影片1](https://github.com/hannah0327/Exchange-Rate-LINE-BOT/assets/130882926/5a433302-0669-431c-883c-fc45b62b1481)
![投影片2](https://github.com/hannah0327/Exchange-Rate-LINE-BOT/assets/130882926/bc5fa752-4ec5-471e-8d47-1fe432befd79)

DEMO影片:
https://github.com/hannah0327/Exchange-Rate-LINE-BOT/assets/130882926/fb76bc27-b0ea-4990-af64-333cb7aae4a0

