# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['tinydeal.com.hk']
    start_urls = ['https://www.tinydeal.com.hk/specials.html']

    def parse(self, response):
        
        for product in response.xpath("//ul[@class = 'productlisting-ul']/div/li"):
            yield{ 
                'title': product.xpath(".//a[@class = 'p_box_title']/text()").get(),
                'url': response.urljoin(product.xpath(".//a[@class = 'p_box_title']/@href").get()),
                'discounted_price' :product.xpath(".//div[@class = 'p_box_price']/span[1]/text()").get(),
                'original_price' :product.xpath(".//div[@class = 'p_box_price']/span[2]/text()").get() }

        next_page = response.xpath("//a[@class = 'nextPage']/@href").get()
        print(next_page)
        if next_page != None:
            yield scrapy.Request(next_page, callback = self.parse, dont_filter = True)    



            