# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from .items import AnjukeItem

class AnjukePipeline(object):

    # 保存数据，创建文件
    def open_spider(self, item):
        self.file = open('anjuke.json','w')

    # item 是对象，需要转成字典来写入文件
    def process_item(self, item, spider):
        if isinstance(item, AnjukeItem):
            str_data = json.dumps(dict(item), ensure_ascii=False) + ',\n'
            self.file.write(str_data.encode('utf-8'))

        return item

    def close_spider(self):
        self.file.close()
