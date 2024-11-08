import json
from homework_spyder.items import AuthorItem, QuoteItem

class DataPipeline:
    quotes = []
    authors = []

    def process_item(self, item, spider):
        if isinstance(item, AuthorItem):
            self.authors.append(dict(item))
        elif isinstance(item, QuoteItem):
            self.quotes.append(dict(item))
        return item

    def close_spider(self, spider):
        with open('quotes.json', 'w', encoding='utf-8') as fd:
            json.dump(self.quotes, fd, ensure_ascii=False, indent=2)
        with open('authors.json', 'w', encoding='utf-8') as fd:
            json.dump(self.authors, fd, ensure_ascii=False, indent=2)