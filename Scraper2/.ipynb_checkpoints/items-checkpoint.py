# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# from scrapy import Field
from scrapy.loader.processors import MapCompose, TakeFirst, Join

# def remove_nt(value):
#   return value.replace('\t','').replace('\n','')

# class SfixSpiderItem(scrapy.Item):

#   link = scrapy.Field(
#         input_processor = MapCompose(str.strip, remove_nt),
#         output_processor= TakeFirst()
#   )
#   price = scrapy.Field(
#         input_processor = MapCompose(str.strip, remove_nt),
#         output_processor= TakeFirst()
#   )

class Scraper2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class WebPageItem(scrapy.Item):
    # specific_url = Field()
    # origin_url = scrapy.Field()
    link_dict = scrapy.Field()
    pass

class WebPolicyItem(scrapy.Item):
    # can be obtained from the host page
    # host = scrapy.Field()
    # label = scrapy.Field() 
    link = scrapy.Field()
    # can only be obtained from the policy page
    title = scrapy.Field()
    url = scrapy.Field()
    last_updated = scrapy.Field()
    text = scrapy.Field()
    # html = scrapy.Field()
    pass

class ExportItem(scrapy.Item):
    text = scrapy.Field()
    updates = scrapy.Field()
    titles = scrapy.Field()
    urls = scrapy.Field()

