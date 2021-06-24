import scrapy


class SetdownSpider(scrapy.Spider):
    name = 'setdown'
    allowed_domains = ['cosersets.com']
    start_urls = ['http://cosersets.com/']

    def parse(self, response):
        pass
