# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeipinhuiItem(scrapy.Item):
    # define the fields for your item here like:
    brand = scrapy.Field()  # 品牌
    title = scrapy.Field()  # 标题
    old_price = scrapy.Field()  # 原价
    new_price = scrapy.Field()  # 现价
    discount = scrapy.Field()  # 折扣
    img_url = scrapy.Field()  # 图片地址
    url = scrapy.Field()  # 链接