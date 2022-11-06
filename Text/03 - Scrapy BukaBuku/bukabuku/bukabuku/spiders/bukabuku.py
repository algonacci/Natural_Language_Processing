import scrapy

class BukaBukuSpider(scrapy.Spider):
    name = 'bukabuku'
    start_urls = ['http://www.bukabuku.com/']

    def parse(self, response):
        for products in response.css('div.product_list_grid_home'):
            yield {
                'title': products.css('div.product_list_title > a::text').get(),
                'url': 'http://www.bukabuku.com' + products.css('div.image > a').attrib['href'],
                'original_price': products.css('div > div.price_discounted::text').get(),
                'discounted_price': products.css('div > div.price::text').get(),
                'image_url': products.css('div.image > a > img').attrib['src'],
            }