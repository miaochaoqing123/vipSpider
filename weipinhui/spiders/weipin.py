# -*- coding: utf-8 -*-
import scrapy
from weipinhui.items import WeipinhuiItem
import urllib.parse

class WeipinSpider(scrapy.Spider):
    name = 'weipin'
    allowed_domains = ['vip.com']
    keyword = input("请输入搜索内容: ")
    start_page = input("请输入开始页: ")
    end_page = input("请输入结束页:")
    start_urls = []
    # 用for循环取得每一页的网址
    for page in range(int(start_page),int(end_page)+1):
        data = {
            "keyword":keyword,
            "page":page
        }
        data = urllib.parse.urlencode(data)
        url = 'https://category.vip.com/suggest.php?'
        urls = url + data
        start_urls.append(urls)

    def parse(self, response):
        div_list = response.xpath("//div[starts-with(@id,'J_pro_')]")
        # print(div_list)
        item = WeipinhuiItem()
        for div in div_list:
            # 用xpath进行解析
            item["brand"] = div.xpath(".//h4/a/span/text()").extract_first()
            item["title"] = div.xpath("./div/h4/a/@title").extract_first()
            item["old_price"] = "¥"+div.xpath(".//del/text()").extract_first()
            item["new_price"] = "¥"+div.xpath(".//div[@class='goods-price-wrapper']/em/span[2]/text()").extract_first()
            item["discount"] = div.xpath("./div/div[@class='goods-info goods-price-info']/span/text()").extract_first()
            item["img_url"] = "http:"+div.xpath(".//div[@class='goods-image']/a/img/@src").extract_first()
            item["url"] = "http:"+div.xpath(".//h4/a/@href").extract_first()
            yield item




