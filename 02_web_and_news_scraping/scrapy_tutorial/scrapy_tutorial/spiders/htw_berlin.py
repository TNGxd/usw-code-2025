import scrapy
from scrapy_tutorial.items import ScrapyTutorialItem

class HtwBerlinSpider(scrapy.Spider):
    name = "htw_berlin"
    allowed_domains: list[str] = ["htw-berlin.de"]
    start_urls = ["https://www.htw-berlin.de/studium/studiengaenge/"]

    def start_requests(self):
        # https://docs.scrapy.org/en/latest/intro/tutorial.html
        for url in self.start_urls:
            # Use the Playwright downloader middleware for each request
            yield scrapy.Request(url, meta={"playwright": True})

    def parse(self, response):
        print("Parsing the response...")

        # TODO: parse the title element and yield it as item

        # get info page per study program
        links = response.css("div.card-container a::attr(href)").getall()
        for link in links:
            if link.endswith("/"):
                yield scrapy.Request(
                    url=link,
                    meta={"playwright": True},
                )