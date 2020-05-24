import scrapy
import logging
from dcardSpider.items import DcardspiderItem
class DcardSpider(scrapy.Spider):
	name = 'DcardSpider'
	allow_domains = 'dcard.tw'
	start_urls = ['https://www.dcard.tw/f']
	def parse(self,response):
		selector = response.xpath('//*[@id="__next"]/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/article')
		for article in selector:
			item = DcardspiderItem()
			item['article'] = article.css('h2').re('.*span>(.*)</span.*')[0]
			item['hyperLink'] = "https://www.dcard.tw" + article.xpath('./h2/a/@href').get()
			item['motion'] = article.xpath('./div[3]/div[1]/div/div[2]/text()').get()
			item['forum'] = article.xpath('./div[1]/div/div[2]/span[1]/text()').get()
			item['response'] = article.xpath('./div[3]/div[2]/span[2]/text()').get()
			item['writer'] = article.xpath('./div[1]/div/div[2]/span[2]/text()').get()
			item['date'] = article.xpath('./div[1]/div/div[2]/span[3]/text()').get()
			yield item
		with open('count.txt','r') as f:
			if [i for i in f.readlines() if "20" in i]:
				return None
		for i in range(10):
			yield scrapy.Request('https://www.dcard.tw/f',callback=self.parse,dont_filter=True)