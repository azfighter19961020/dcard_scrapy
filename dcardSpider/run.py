from scrapy import cmdline
import os
import logging
if os.path.isfile('count.txt'):
	os.remove('count.txt')
	logging.info('count.txt is removed.')
cmdline.execute('scrapy crawl DcardSpider'.split())