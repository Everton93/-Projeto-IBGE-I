import sys
import asyncio
import logging
from Parse_IBGE import ParseEstadosIBGE as parseEstados
from Parse_IBGE import ParseMunicipiosIBGE as parseMunicipios
import Requests_IBGE.RequestsIBGE as searchData
import logging


async def main_requests() -> None:

    try:
        taskConfig = asyncio.create_task(coro= configPython())
        await taskConfig
        taskGetPageIBGE = asyncio.create_task(
            coro=searchData.obterPaginaIbge())
        htmlPage = await taskGetPageIBGE
        taskGetStates = asyncio.create_task(
            coro=parseEstados.obterListaEstados(htmlPage))
        listStates = await taskGetStates
        taskGetCities = asyncio.create_task(
            coro=parseMunicipios.obterListaMunicipios(htmlPage,listStates))
        citiesListRequest = await taskGetCities

    except Exception as e:
        logging.error(e)
        
async def configPython():
    logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')
    logging.debug("initialize configuration")        

if __name__ == "__main__":
    asyncio.run(main_requests())



