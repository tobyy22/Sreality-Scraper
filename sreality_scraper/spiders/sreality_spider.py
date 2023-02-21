import scrapy
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.project import get_project_settings

from sreality_scraper.items import SrealityItem


class FlatSpider(scrapy.Spider):
    name = 'sreality'
    

    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&sort=0&per_page=100' + '&page='+str(page)+''for page in range(1, 6)]

    def parse(self, response):
         i = 0
         jsonresponse = response.json()
         for item in jsonresponse["_embedded"]['estates']:
             current_imgs = item["_links"]["images"]
             current_img = None
             if current_imgs != []:
                 current_img = current_imgs[0]
             sri = SrealityItem()
             sri["name"] = item["name"]
             sri["image"] = current_img

             yield sri


if __name__ == "__main__":
    

    settings = dict()
    settings['ITEM_PIPELINES'] = { 'sreality_scraper.pipelines.SrealityPipeline': 300,}


    process = CrawlerProcess(settings)


    process.crawl(FlatSpider)
    process.start()
