import scrapy

class SrcSpider(scrapy.Spider):
    name = "src_spider"
    allowed_domains = ["google.com"]
    start_urls = ["https://www.google.com/search?q=your+query"]

    def _init_(self, search_term='', *args, **kwargs):
        super(SrcSpider, self)._init_(*args, **kwargs)
        self.search_term = search_term
        self.result_count = 0  # Contador para limitar os resultados
        self.max_results = 2   # Limite de 2 resultados

    def start_requests(self):
        # Montar a URL de pesquisa do Google com base no termo de busca
        url = f"https://www.google.com/search?q={self.search_term}"
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for item in response.css('div.TzHB6b cLjAic K7khPe'):  
            title = item.css('h3::text').get()
            link = item.css('a::attr(href)').get()

            # Contar os resultados e parar após o quinto
            if self.result_count < self.max_results and title and link:
                self.result_count += 1
                yield {'title': title, 'link': link}

            # Interromper o loop após pegar 5 resultados
            if self.result_count >= self.max_results:
                break