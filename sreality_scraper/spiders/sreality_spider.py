import scrapy
from scrapy.crawler import CrawlerProcess
from sreality_scraper.items import SrealityItem

class FlatSpider(scrapy.Spider):
    name = 'sreality'
    start_urls = [f'https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&sort=0&per_page=100&page={page}' for page in range(1, 6)]

    def parse(self, response):
        jsonresponse = response.json()
        for item in jsonresponse["_embedded"]['estates']:
            current_img = None
            current_imgs = item["_links"]["images"]
            if current_imgs:
                current_img = current_imgs[0]
            yield SrealityItem(name=item["name"], image=current_img)

if __name__ == "__main__":
    settings = {'ITEM_PIPELINES': {'sreality_scraper.pipelines.SrealityPipeline': 300}}
    process = CrawlerProcess(settings)
    process.crawl(FlatSpider)
    process.start()