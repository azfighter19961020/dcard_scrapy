# dcard_scrapy
# crawler for dcard by scrapy
# 使用scrapy & selenium爬取dcard熱門文章
<img src="https://github.com/charlie11438/dcard_scrapy/blob/master/sql.png?raw=true" />
- 修改downloadermiddleware讓scrapy與selenium交互，達到捲動效果
<br></br>
- 透過pymysql將資料儲存在mysql裡面，重複的就更新回應以及心情數
<br></br>
- 由於捲動會造成前面data流失，所以使用count來控制捲動次數以及終止條件
<br></br>
## 檔案結構<br>
├─dcardSpider<br>
│  count.txt   終止所需文件<br>
│  items.py    創建item Field供儲存<br>
│  middlewares.py  中間器，修改downloadmiddleware<br>
│  pipelines.py   資料持久化的運作，與pymysql交互<br>
│  run.py      命令列執行py檔，scrapy.cmdline<br>
│  settings.py scrapy設定，打開downloadmiddleware以及pipeline<br>
│  test.py     文件測試檔<br>
│  __init__.py<br>
│<br>
├─spiders<br>
│  │  dcardSpider.py   spider主檔<br>
│  │  __init__.py<br>
├──<br>
