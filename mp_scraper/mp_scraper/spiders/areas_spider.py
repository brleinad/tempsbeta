import scrapy

class AreasSpider(scrapy.Spider):
    name = 'areas'
    start_urls = [
      # 'https://www.mountainproject.com/route-guide',
      # 'https://www.mountainproject.com/area/106142016/quebec', # just for testing
      # 'https://www.mountainproject.com/area/120619194/vallee-du-bras-du-nord', # just for testing
      'https://www.mountainproject.com/area/110151418/mont-wright',
    ]

    def parse(self, response):
        yield {
          'area': ' '.join(response.css('h1::text').get().split()),
          'location': ' '.join(response.css('.description-details>tr:nth-child(2)>td:nth-child(2)::text ').get().split()),
          'url': response.url,
        }
        for next_area in response.css('.lef-nav-row>a::attr(href)'):
          yield response.follow(next_area, callback=self.parse)

