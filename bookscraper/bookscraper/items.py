# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    availability = scrapy.Field()



# class BookItem(scrapy.Item):
#     title = scrapy.Field()
#     price = scrapy.Field()
#     rating = scrapy.Field()
#     stock = scrapy.Field()
#     upc = scrapy.Field()
#     product_type = scrapy.Field()
#     tax = scrapy.Field()
#     reviews = scrapy.Field()

