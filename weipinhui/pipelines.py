# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import urllib.request

import pymysql
from scrapy.utils.project import get_project_settings

class WeipinhuiPipeline(object):
    def __init__(self):
        self.fp = open("weipin.json","w",encoding="utf-8")
        self.items = []

    def open_spider(self,spider):
        pass

    def process_item(self, item, spider):
        self.items.append(dict(item))
        return item

    def close_spider(self,spider):
        # print(len(self.items))
        # 下载图片
        # for item in self.items:
        #     for i in item:
        #         if item["img_url"]:
        #             url = item["img_url"]
        #             img_name = url.split("/")[-1]
        #             urllib.request.urlretrieve(url,"./img/"+img_name)
        # 保存json格式数据
        self.fp.write(json.dumps(self.items,ensure_ascii=False))
        self.fp.close()


# 定义一个类用来写入数据库
class MysqlPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        self.host = settings["DB_HOST"]
        self.port = settings["DB_PORT"]
        self.user = settings["DB_USER"]
        self.pwd = settings["DB_PWD"]
        self.name = settings["DB_NAME"]
        self.charset = settings["DB_CHARSET"]
        self.connect()

    def connect(self):
        self.conn = pymysql.connect(host=self.host,
                                    port=self.port,
                                    user=self.user,
                                    password=self.pwd,
                                    db=self.name,
                                    charset=self.charset)
        # 创建游标,用于对数据库进行操作
        self.cursor = self.conn.cursor()

    def open_spider(self,spider):
        pass

    def process_item(self,item,spider):
        # 创建一个sql语句
        if isinstance:
            # sql = "INSERT INTO goods VALUES(NULL ,\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');"%(item["brand"],item["title"],item["new_price"],item["discount"],item["old_price"],item["img_url"],item["url"])
            sql = "INSERT INTO goods VALUES(NULL ,'%s','%s','%s','%s','%s','%s','%s');" % (item["brand"], item["title"], item["new_price"], item["discount"], item["old_price"], item["img_url"],item["url"])
            self.cursor.execute(sql)
            self.conn.commit()
            return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()