# -*- coding: utf-8 -*-
import scrapy
# 从上级目录导入item
from ..items import AnjukeItem

class SzzufangSpider(scrapy.Spider):
    name = 'szzufang'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://sz.zu.anjuke.com/']

    def parse(self, response):
        # 提取节点列表
        node_list = response.xpath('//*[@id="list-content"]/div[@class="zu-itemmod"]')
        # print(len(node_list))
        # 遍历节点，提取响应数据
        for node in node_list:
            # 实例化item对象，用来存储数据
            item = AnjukeItem()
            item['name'] = node.xpath('./div[1]/h3/a/text()').extract()[0].strip()
            item['detail_url'] = node.xpath('./div[1]/h3/a/@href').extract()[0]
            item['mold'] = node.xpath('./div[1]/p[1]/text()').extract()[0].strip()
            item['traffic'] = node.xpath('./div[1]/p[@class="details-item bot-tag"]/span/text()').extract()[0]
            # print(item)
            # 直接把item返回给引擎
            yield item

        # 实现翻页功能，定位下一页
        next_url = response.xpath('//div/a[@class="aNxt"]/@href').extract()[0]
        # 手动发送请求，定位下一页，回调函数只写函数名，不加()
        yield scrapy.Request(
            next_url,
            callback=self.parse
        )
