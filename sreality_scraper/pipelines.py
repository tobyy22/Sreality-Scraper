import psycopg2

from sreality_scraper.settings import HOST, DB_NAME, USER, PASSWORD
from sreality_scraper.database import database

class SrealityPipeline:
    def process_item(self, item, spider):
        name = item['name']
        image = item['image']["href"]
        database.insert_item(name, image)
        return item