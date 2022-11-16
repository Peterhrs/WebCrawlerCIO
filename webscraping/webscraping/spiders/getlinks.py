import scrapy

class getlinksSpider(scrapy.Spider):
    name = 'getlinks'
    start_urls = ['https://www.alura.com.br/cursos-online-programacao']

    def __init__(self, **kwargs):
        self.total_links = 0
        super().__init__(**kwargs)

    #pega as tags inteiras que tenham htts dos sites 
    def PegarDadosBruntos(self, response):
        Seletor = "//a[contains(@href,'http')]" 
        DadosBrutos = []
        DadosBrutos = response.xpath(Seletor).getall()
        return DadosBrutos

    #verifica em qual elemento da lista quebrada de tags o link esta
    def limparLinksFinais(self, dadoseparado, links):
        continuar = True
        cont = 1
        #enquanto ele nao capturar o link o while continua
        while continuar:
            if dadoseparado[cont].startswith('http'):
                links.append(dadoseparado[cont])
                continuar = False
            else:
                cont = cont + 1
        return links

    #executa o crawler
    def parse(self, response):
        
        links = []
        dados  = self.PegarDadosBruntos(response)

        for dado in dados:
            dado_quebrado = dado.split('"')
            links = self.limparLinksFinais(dado_quebrado, links)
        self.total_links += len(links)
        
        for link in links:
            yield{
            'link': link
            }
            url = link
            yield scrapy.Request(url = url, callback=self.parse)
