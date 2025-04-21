import scrapy


class HtwBerlinSpider(scrapy.Spider):
    name = "htw_berlin"
    allowed_domains: list[str] = []
    start_urls = ["https://www.htw-berlin.de/studium/studiengaenge/"]

    def start_requests(self):
        # https://docs.scrapy.org/en/latest/intro/tutorial.html
        for url in self.start_urls:
            # Use the Playwright downloader middleware for each request
            yield scrapy.Request(url, meta={"playwright": True})

    def parse(self, response):
        print("Parsing the response...")
        titles = response.css("div.card-headline").getall()
        for title in titles:
            print(title)

        # get info page per study program
        links = response.css("div.card-container a::attr(href)").getall()
        for link in links:
            yield scrapy.Request(
                url=link,
                meta={"playwright": True},
            )