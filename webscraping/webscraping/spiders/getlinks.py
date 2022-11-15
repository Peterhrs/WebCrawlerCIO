import scrapy

class getlinksSpider(scrapy.Spider):
    name = 'getlinks'
    start_urls = ['https://www.alura.com.br/cursos-online-programacao']

    #pega as tags inteiras que tenham htts dos sites 
    def PegarDadosBruntos(self, response):

        Seletor = "//a[contains(@href,'http')]" 
        DadosBrutos = []
        DadosBrutos = response.xpath(Seletor).getall()
        return DadosBrutos

    #quebra as tags em intervalos, dividindo pelo paramentro aspas duplas
    def quebrarDadosBrutos(self, dados,n):
            parseallink = dados[n]
            return parseallink.split('"')

    #verifica em qual elemento da lista quebrada de tags o link esta
    def limparLinksFinais(self, dadoseparado, continuar,links):
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
        n = 0
        dados  = self.PegarDadosBruntos(response)
        for i in dados:
            if i == dados:
                continuar = False
            else:
                continuar = True

            dadoseparado = self.quebrarDadosBrutos(dados,n)
            n = n + 1
            links = self.limparLinksFinais(dadoseparado,continuar,links)

        numeros = 1
        for p in links:
            yield{
            'link': links[numeros]
            }
            url = links[numeros]
            yield scrapy.Request(url = url, callback=self.parse)
            numeros = numeros + 1

