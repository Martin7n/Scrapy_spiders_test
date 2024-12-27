from gc import callbacks
from itertools import product

import scrapy
from scrapy.spiders import CrawlSpider



class BookScraper(scrapy.Spider):
    name = 'bookscraper'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']


    def parse(self, response):
        prods =  response.css(".product_pod")

        for product in prods:
            relative_url = product.css('a').attrib["href"]

            if 'catalogue' in relative_url:
                book_url = 'https://books.toscrape.com/' + relative_url
            else:
                book_url =  self.start_urls[0] + "catalogue/" + relative_url
            yield response.follow(book_url, callback=self.parse_book_page)

        next = response.css('li.next>a').attrib['href']
        if next is not None:
            if 'catalogue' in next:
                next_page_url = self.start_urls[0] + next
            else:
                next_page_url =  self.start_urls[0] + "catalogue/" + next
            yield response.follow(next_page_url, callback=self.parse)

        # for product in prods:
        #     yield{
        #         "short_name": product.css('a::text').get(),
        #         "title":  product.css('a::attr(title)').get(),
        #         'price': product.css('.price_color::text').get(),
        #         'url': product.css('a').attrib["href"],
        #         'availability': product.css('p.instock.availability::text').getall(),
        #     }

        next = response.css('li.next>a').attrib['href']


        if next is not None:
            if 'catalogue' in next:
                next_page_url = self.start_urls[0] + next
            else:
                next_page_url =  self.start_urls[0] + "catalogue/" + next
            yield response.follow(next_page_url, callback=self.parse)

    def parse_book_page(self, response):

        yield{
        "title":  response.css("h1::text").get(),
        "price": response.css("table tr td::text")[2].get(),
        "availability": response.css("table tr td::text")[5].get(),
        "description": response.xpath("//div[@id='product_description']/following-sibling::p/text()").get()
        }

