# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class H8DsftScrapItem(scrapy.Item):
    
    title = scrapy.Field()
    rating = scrapy.Field()
    description = scrapy.Field()
    votes = scrapy.Field()
    poster = scrapy.Field()