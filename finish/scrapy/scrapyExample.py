# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'ptt'
    allowed_domains = ['ptt.com']
    start_urls = ['http://www.ptt.cc/bbs/Food/index.html',
                  'http://www.ptt.cc/bbs/movie/index.html']

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
