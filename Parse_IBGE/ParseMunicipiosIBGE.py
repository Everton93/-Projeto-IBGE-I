import logging
import asyncio
from Model.Municipio import Municipio
from Model.Estados import Estados
from bs4 import BeautifulSoup as bs
from asyncio import Task


async def obterListaMunicipios(html, listStates):
    try:
        logging.info('Parse Cities in IBGE ...')
        pages = bs(html, 'lxml').find_all({'table': 'container-uf'})
        pages.pop(00)
        municipioList = list()      
        i = 0      
        for page in pages:        
            atribute = page.find_all({'tr': 'municipio data-line'})
            estado = await obterEstado(listStates,i)
            i +=1
            for atr in atribute:                    
                municipio = Municipio(
                    atr.find({'a': 'blank'}).text,
                    atr.find('td', {'class': 'numero'}).text,
                    estado)
                municipioList.append(municipio)

        logging.info('Parse Cities Sucessfuly !!!')
        return municipioList
    except Exception as error:
        raise Exception(error)
    
async def obterEstado(listStates, i):
    return listStates[i]  