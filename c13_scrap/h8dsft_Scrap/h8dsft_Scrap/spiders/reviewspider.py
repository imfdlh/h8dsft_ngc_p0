import scrapy
from h8dsft_Scrap.items import H8DsftScrapItem

class ReviewspiderSpider(scrapy.Spider):
    name = 'reviewspiderMultiple'
    start_urls = ['https://www.imdb.com/search/title/?genres=animation']
    
    for i in range(51, 10000, 50):
        start_urls.append('https://www.imdb.com/search/title/?genres=animation&start=' + str(i) + '&ref_=adv_nxt')

    def parse(self, response):
        for href in response.xpath('//h3[@class="lister-item-header"]/a/@href'):
            url = 'https://www.imdb.com/' + href.extract()
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        item = H8DsftScrapItem()

        item['title'] = response.xpath('//h1[@data-testid="hero-title-block__title"]/text()').extract()[0]
        item['rating'] = response.xpath('//div[@data-testid="hero-rating-bar__aggregate-rating__score"]/span[1]/text()').extract()[0]
        item['description'] = response.xpath('//span[@data-testid="plot-xl"]/text()').extract()[0].strip()
        item['votes'] = response.xpath('//div[@data-testid="hero-rating-bar__aggregate-rating__score"]/following-sibling::div/text()').extract()[0]
        item['poster'] = response.xpath('//img[@class="ipc-image"]/@src').extract()[0]

        yield item