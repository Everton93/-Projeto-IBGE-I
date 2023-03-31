from bs4 import BeautifulSoup as bs
from Model.Estados import Estados  
import logging

async def obterListaEstados(html):
    try:
        logging.info('Parse States IBGE ...')
        page = bs(html, 'lxml').find({'tbody': 'codigos-list'})
        atributesPage = page.find_all('tr')
        estadoList = list()

        for attributes in atributesPage:
            estado = Estados(str(attributes.contents[1].text).replace(
            'ver municípios', ''), attributes.contents[0].text)
            estadoList.append(estado)

        logging.info('Parse States Sucessfuly !!!')
        return estadoList

    except Exception as error:
        logging.error(error)
        return  error.args