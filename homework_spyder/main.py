from scrapy.crawler import CrawlerProcess
from homework_spyder.spiders.quotes_spider import QuotesSpider
from homework_spyder.pipelines import DataPipeline

if __name__ == '__main__':
    process = CrawlerProcess(settings={
        "ITEM_PIPELINES": {
            DataPipeline: 300,
        },
    })
    process.crawl(QuotesSpider)
    process.start()