from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .spiders.src_finder_spider import SrcSpider

def run_spider(search_term):
    process = CrawlerProcess(get_project_settings())
    process.crawl(SrcSpider, search_term=search_term)
    process.start()

    # Aqui você pode coletar os resultados e retorná-los
    return process.spider.crawled_data
