import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
import pandas as pd


companies = pd.read_csv('fortune500.csv', usecols = [2], header = None)

companies_array = companies.to_numpy().flatten()

companies_array = [i for i in companies_array[1:]]
print(companies_array)



class LinkSpider(scrapy.spiders.CrawlSpider):
	name = 'linkspider'

	start_urls=companies_array



	rules = [Rule(LinkExtractor(allow='terms'), callback='parse_item', follow = False)]

	def parse_item(self, response):
		yield {
			'url': response.url,
			'text':" ".join("".join(response.selector.xpath("//body//text()").extract()).strip().split())
		}

