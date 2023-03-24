
import logging
import asyncio
from Model.Municipio import Municipio
import sys
from bs4 import BeautifulSoup as bs


async def obterListaMunicipios(html, listStates):
    try:
        logging.info('Parse Cities in IBGE ...')
        pages = bs(html, 'lxml').find_all({'table': 'container-uf'})
        pages.pop(00)
        municipioList = list()

        for page in pages:

            cidade = await replaceIgbe(page)
            atribute = page.find_all({'tr': 'municipio data-line'})
            for atr in atribute:
                municipio = Municipio(
                    atr.find({'a': 'blank'}).text,
                    atr.find('td', {'class': 'numero'}).text,
                    cidade)
                municipioList.append(municipio)

        logging.info('Parse Cities Sucess !!!')
        return municipioList
    except Exception as error:
        return logging.error(error)


async def replaceIgbe(page) -> str:
    if str(page.find({'th'}).text).__contains__('Municípios do '):
        return str(page.find({'th'}).text).replace('Municípios do ', '')

    if str(page.find({'th'}).text).__contains__('Municípios de '):
        return str(page.find({'th'}).text).replace('Municípios de ', '')

    if str(page.find({'th'}).text).__contains__('Municípios da '):
        return str(page.find({'th'}).text).replace('Municípios da ', '')
