import scrapy
from scrapy.spiders import CrawlSpider


class BookScraper(scrapy.Spider):
    name = 'bookscraper'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        prods =  response.css(".product_pod")
        for product in prods:
            yield{
                "short_name": product.css('a::text').get(),
                "title":  product.css('a::attr(title)').get(),
                'price': product.css('.price_color::text').get(),
                'url': product.css('a').attrib["href"],
                'availability': product.css('p.instock.availability::text').getall(),
            }



