import asyncio
import logging
from Parse_IBGE import ParseEstadosIBGE as parseEstados
from Parse_IBGE import ParseMunicipiosIBGE as parseMunicipios
from SendData import SendDataIBGE as sendIBGE
import Requests_IBGE.RequestsIBGE as searchData
from dotenv import load_dotenv, find_dotenv
import os
import boto 

# from azure.servicebus.aio import ServiceBusClient as client



async def main(senderService) -> None:

    try:
        pageHtml = await searchData.obterPaginaIbge()
        listStates = await parseEstados.obterListaEstados(pageHtml)
        citiesListRequest = await parseMunicipios.obterListaMunicipios(pageHtml, listStates)
        await sendIBGE.sendMessage(senderService, citiesListRequest)

        logging.debug('finished !!!')

    except Exception as error:
        logging.error(error)
    
if __name__ == "__main__":
    
    logging.debug("initialize configuration")
    
    load_dotenv()
    logging.basicConfig(level=logging.DEBUG,
                        format='%(name)s - %(levelname)s - %(message)s')
    
    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler()) 
    logger.setLevel(logging.DEBUG)
    logging.getLogger('boto').setLevel(logging.CRITICAL)   
    
    

    config = boto.connect_sqs(aws_access_key_id= os.getenv('AWS_SQS_ACESS_KEY'),
                                aws_secret_access_key= os.getenv('AWS_SQS_SECRET_KEY'))       
    
    _senderService = boto.sqs.queue.Queue(connection=config, 
                                         url=os.getenv('AWS_SQS_URL'))
            
asyncio.run(main(_senderService))
