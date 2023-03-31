import asyncio
import logging
from Parse_IBGE import ParseEstadosIBGE as parseEstados
from Parse_IBGE import ParseMunicipiosIBGE as parseMunicipios
from SendData import SendDataIBGE as sendIBGE
import Requests_IBGE.RequestsIBGE as searchData
from dotenv import load_dotenv , find_dotenv
import os 
from azure.servicebus.aio import ServiceBusClient as client

async def main(_serviceSender) -> None:

    try:       
        pageHtml = await searchData.obterPaginaIbge()       
        pageList = await parseEstados.obterListaEstados(pageHtml)
        listStates = await parseEstados.obterListaEstados(pageHtml)
        citiesListRequest = await parseMunicipios.obterListaMunicipios(pageHtml,listStates)

        await sendIBGE.sendMessage(_serviceSender, citiesListRequest)
                
        logging.debug('finished !!!')
        
    except Exception as error:
        logging.error(error)
        return error.args
        
    
if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')        
    logging.debug("initialize configuration")  
    service = client.from_connection_string(os.getenv('SERVICE_BUS_CONNECTION_STR'))     
    senderService = service.get_queue_sender(os.getenv('SERVICE_BUS_QUEUE_NAME'))          
    asyncio.run(main(senderService))
    
