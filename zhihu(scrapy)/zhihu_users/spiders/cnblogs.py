# -*- coding: utf-8 -*-
import scrapy

class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['cnblogs.com']
    start_urls = ['https://www.cnblogs.com/cate/mysql/']
    # def start_requests(self):
    #     urls = ['https://www.cnblogs.com/cate/mysql/']
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.text)
