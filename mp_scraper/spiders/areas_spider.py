import scrapy
from pymongo import MongoClient
from dotenv import load_dotenv
import os


class AreasSpider(scrapy.Spider):
    name = 'areas'
    start_urls = [
        # 'https://www.mountainproject.com/route-guide', # the whole shebang
        # just for testing
        'https://www.mountainproject.com/area/106142016/quebec',
        # 'https://www.mountainproject.com/area/120619194/vallee-du-bras-du-nord',
        # 'https://www.mountainproject.com/area/110151418/mont-wright',
    ]
    areas = None


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

        client = MongoClient(connection_string)
        self.areas = client.tempsbeta.areas
        self.areas.delete_many({}) # TODO: find a way to not have to reset the DB every time?

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

        if not self._is_there_a_nearby_area(area):
            yield area
            self.areas.insert_one(area)

        for next_area in response.css('.lef-nav-row>a::attr(href)'):
            yield response.follow(next_area, callback=self.parse)

    def clean_string(self, string):
        """
        removes all new lines, spaces, tabs from a string
        """
        return ' '.join(string.split())

    def _is_there_a_nearby_area(self, area):
        """
        is there already an area near the given area?
        """
        nearby_distance_in_meters = 1
        print('AREA ', area)
        query = {
            'location':
                {'$near':
                    {
                        '$geometry': {'type': 'Point', 'coordinates': area['location']['coordinates']},
                        '$minDistance': nearby_distance_in_meters,
                        '$maxDistance': nearby_distance_in_meters + 5000,
                    }
                }
        }
        results = self.areas.find_one(query)
        print('RESULTS ', results)

        return results

