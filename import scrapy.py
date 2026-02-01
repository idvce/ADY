import scrapy

class CarsSpider(scrapy.Spider):
    name = "cars"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com/used-cars-danang?page=1"]

    def parse(self, response):
        # 1. loop all car cards on the page
        for card in response.css("div.car-card"):
            yield {
                "title": card.css("h2.car-title::text").get(default="N/A").strip(),
                "price": card.css("p.car-price::text").get(default="N/A").strip(),
                "page_url": response.url,
            }

        # 2. follow 'next page' link automatically
        next_page = response.css("a.next-page::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
