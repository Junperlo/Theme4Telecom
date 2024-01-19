import scrapy

class RankingSpider(scrapy.Spider):
    name = 'ranking_spider'
    allowed_domains = ['www.shanghairanking.com']
    start_urls = ['https://www.shanghairanking.com/rankings/arwu/2022']

    def parse(self, response):
        rows = response.xpath('//tbody/tr')
        for row in rows:
            rank = row.xpath('.//td[1]/div/text()').get()
            uni_name = row.xpath('.//td[2]/div/div[2]/span/text()').get()
            yield {'Rank': rank, 'University Name': uni_name}
