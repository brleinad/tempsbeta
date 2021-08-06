import scrapy
from pymongo import MongoClient
from dotenv import load_dotenv
import os


class AreasSpider(scrapy.Spider):
    name = 'areas'
    start_urls = [
        # 'https://www.mountainproject.com/route-guide',
        # 'https://www.mountainproject.com/area/106142016/quebec', # just for testing
        # 'https://www.mountainproject.com/area/120619194/vallee-du-bras-du-nord', # just for testing
        'https://www.mountainproject.com/area/110151418/mont-wright',
    ]

    def __init__(self, category=None, *args, **kwargs):
        super(AreasSpider, self).__init__(*args, **kwargs)
        load_dotenv()
        self.initialize_mongodb()

    def initialize_mongodb(self):
        print('Initializing Mongo')
        MONGODB_USER = os.environ["MONGODB_USER"]
        MONGODB_PASSWORD = os.environ["MONGODB_PASSWORD"]
        MONGODB_CLUSTER = os.environ["MONGODB_CLUSTER"]
        connection_string = f'mongodb+srv://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_CLUSTER}?retryWrites=true&w=majority'
        self.client = MongoClient(connection_string)
        self.db = self.client.tempsbeta
        self.areas = self.db.areas
        print('MongoDB ready')

    def parse(self, response):
        print(response.css('#route-chart'))
        coordinates = self.clean_string(response.css('.description-details>tr:nth-child(2)>td:nth-child(2)::text ').get())
        coordinates = coordinates.split(',')
        coordinates = [float(numeric_string) for numeric_string in coordinates]
        area = {
            'name': self.clean_string(response.css('h1::text').get()),
            'url': response.url,
            'location': {
                'type': 'Point',
                'coordinates': coordinates[::-1]
            },
        }
        yield area
        self.areas.insert_one(area)
        for next_area in response.css('.lef-nav-row>a::attr(href)'):
            yield response.follow(next_area, callback=self.parse)

    def clean_string(self, string):
        """
        removes all new lines, spaces, tabs from a string
        """
        return ' '.join(string.split())
