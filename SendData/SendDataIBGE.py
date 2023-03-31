import logging
from azure.servicebus import ServiceBusMessage
import json
import jsonpickle


async def sendMessage(senderService, citiesList) -> None:

    try:
        jsonpickle.set_preferred_backend('json')
        jsonpickle.set_encoder_options('json', ensure_ascii=False)

        logging.debug('sending messages ...')

        for city in citiesList:
            cityJsonMessage = jsonpickle.dumps(city, unpicklable=False)
            message = ServiceBusMessage(cityJsonMessage)
            await senderService.send_messages(message)

        logging.debug('send message is sucessfuly !!!')

    except Exception as error:
        logging.error(error)
        return error.args
