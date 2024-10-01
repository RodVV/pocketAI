import scrapy

class SrcSpider(scrapy.Spider):
    name = "src_finder_spider"

    def __init__(self, search_term=None, *args, **kwargs):
        super(SrcSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f'https://www.google.com/search?q={search_term}']  
    def parse(self, response):
        results = []
        for item in response.css('div.result'):  # Exemplo de seleção de item
            title = item.css('h2::text').get()
            link = item.css('a::attr(href)').get()
            results.append({'title': title, 'link': link})
        
        # Retorna os resultados para o pipeline ou para o processo seguinte
        yield {'results': results}
