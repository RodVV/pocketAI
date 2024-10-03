from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy import signals
from scrapy.signalmanager import dispatcher
from twisted.internet import reactor, defer
from twisted.internet.task import react  # Importa para executar sem bloquear o reactor
from .spiders.src_finder_spider import SrcSpider

crawled_data = []  # Variável global para armazenar os resultados

# Função que irá coletar os itens raspados
def crawler_results(signal, sender, item, response, spider):
    crawled_data.append(item)

# Função assíncrona que irá rodar o spider
@defer.inlineCallbacks
def crawl_spider(search_term):
    global crawled_data
    crawled_data = []  # Limpar os dados antes de cada execução

    # Configurar o Scrapy para rodar com um Runner
    runner = CrawlerRunner(get_project_settings())
    
    # Conectar o sinal que captura os dados raspados
    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    # Executar o spider de forma assíncrona
    yield runner.crawl(SrcSpider, search_term=search_term)

# Função para rodar o spider e retornar os dados coletados
def run_spider_and_return_data(search_term):
    global crawled_data
    
    # Verificar se o reactor já está rodando
    if not reactor.running:
        # Executar o spider usando a função 'react' para garantir que o reactor não seja bloqueado
        react(lambda reactor: crawl_spider(search_term))  # Iniciar o reactor sem bloquear
    
    # Retornar os dados coletados após o término
    return crawled_data