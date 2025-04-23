# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from bs4 import BeautifulSoup

class ScrapyTutorialPipeline:
    def open_spider(self, spider):
        self.file = None

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        # TODO: extract the text from title field in the item,
        # and add it to a text file "studiengaenge.txt"
        return item
