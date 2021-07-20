import scrapy

class AreasSpider(scrapy.Spider):
    name = 'areas'
    start_urls = [
            #'https://www.mountainproject.com/route-guide',
            'https://www.mountainproject.com/area/106142016/quebec',
            ]

    def parse(self, response):
        yield {'area': response.css('h1::text').extract_first()}
        for next_area in response.css('.lef-nav-row>a::attr(href)'):
          yield response.follow(next_area, callback=self.parse)

