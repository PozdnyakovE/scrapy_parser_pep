import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps = response.css('a[href^="pep-"]')
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_info = response.css('h1.page-title::text').get()
        data = {
            'number': pep_info.split(" – ")[0][4:],
            'name': pep_info.split(" – ")[1],
            'status': response.css(
                'dt:contains("Status") + dd > abbr::text'
            ).get(),
        }
        yield PepParseItem(data)
