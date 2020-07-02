import scrapy
from scrapy.loader import ItemLoader


# from demo_project.items import QuoteItem


class GoodReadsSpider(scrapy.Spider):
    # identity
    name = "manufacturer"

    start_urls = [
        'https://www.justdial.com/Delhi/Solar-Panel-Manufacturers/nct-10444072/page-1'
    ]

    # Response
    def parse(self, response):

        for quote in response.xpath("//li[@class='cntanr']"):
            yield {
                # loader= ItemLoader(item=QuoteItem(), selector=quote, response=response)
                'company_name': quote.xpath(".//span[@class='lng_cont_name']").extract_first(),
                'contactno': quote.xpath(".//p[@class='contact-info ']//span//span").extract(),
                'Adress': quote.xpath(".//span[@class='cont_fl_addr']/text()").extract_first()
            }

            # /quotes?page=2
        next_page = response.xpath("//a[@rel='next']/@href").extract_first()

        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)
