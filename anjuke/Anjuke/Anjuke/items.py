# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnjukeItem(scrapy.Item):
    # define the fields for your item here like:
    # 名称，详情链接，大小，楼层，地点，经纪人
    name = scrapy.Field()
    detail_url = scrapy.Field()
    mold = scrapy.Field()
    traffic = scrapy.Field()


