
# WEBCRAWLER

A ideia nesse projeto era construir um webscraping que capturasse apartir de um link inicial outros links e mineirasse
mais e mais links, ele cumpre as especificacoes mas na aba de melhoria podera ver que ha muitas coisas ha serem feitas!
utilizei python e o framework scrapy pois o scrapy se trata de um framework dedicado a criacao de webscraping fazendo
com que tanto a codificao fosse mais simples como a execucao fosse mais leve e mais rapida.
principalmente comparada a proposta inicial que foi fazer com selenium.
todo o projeto desde estudo para criacao ate um modelo estavel foi desenvolvido em 4 dias (11/11, 12/11, 13/11, 14/11) com
aproximadamente 40 horas de investimento.


## Ambiente
python 3.8.8

Scrapy 2.7.1

SQliteStudio  3.3.3
```bash
pip install -r requirements.txt

```
## Rodando localmente
```
1-Crie um clone do projeto localmente
2-Acesse o terminal na pasta do projeto
3-Rode o comando "scrapy crawl getLinks"
obs: como o projeto nao esta totalmente finalizado para parar 
a execucao utilize o comando "CRTL + C"
4-acesse o sqlitestudio abra o arquivo "bdCrawlerLinks", click na
tabela e depois e assim conseguira ver todos os links validos salvos
```

## Melhorias futuras

Aqui listarei melhorias que por motivo do meu conhecimento inicial
no scrapy ou no pyhton ainda nao puderam ser completadas
```
- pipeline para a funcao manipular o link recebido direto da tag
- criar uma funcao para ser colocado o link pelo usuario
- deixar com que o usuario escolha qual a melhor forma de guardar os
    links (aquivo csv, com sqlite(relacional) ou mongodb (nao relacional))
- uma funcao delimitadora para que o software tenha um limite ou break
- uma funcao para que os links repetidos nao sejam acessados ou guardados
- fazer com que o banco guarde as informacoes da origem dos links para saber
- qual foi o link incial ou filtrar por arvore genealogica os links
```

