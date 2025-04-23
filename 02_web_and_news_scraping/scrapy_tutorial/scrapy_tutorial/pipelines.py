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
        self.file = open("studiengaenge.txt", "w")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = BeautifulSoup(item["title"], "html.parser").get_text() + "\n"
        self.file.write(line)
        return item
