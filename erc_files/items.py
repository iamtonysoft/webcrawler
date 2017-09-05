# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ErcFilesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	issuance = scrapy.Field()
	case = scrapy.Field()
	pdf = scrapy.Field()
