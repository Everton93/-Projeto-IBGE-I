import aiohttp
import logging


headersGetPageCities = {
            "Host": "www.ibge.gov.br",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"                                  
            }

async def obterPaginaIbge() -> str:

    base_url = 'http://www.ibge.gov.br/explica/codigos-dos-municipios.php'

    try:
        logging.info('Getting page IBGE ...')

        async with aiohttp.ClientSession() as session:

            async with session.get(base_url,headers=headersGetPageCities) as response:

                if response.status != 200:
                    logging.critical(response.text)
                    raise aiohttp.ClientResponseError(response.status, response.text)
                else:
                    html = await response.text()
                    logging.info('Getting Page Sucessfuly !!!')
                    return html

    except Exception as error:
        
