import logging
import jsonpickle
import os


async def sendMessage(senderService, citiesList) -> None:

    try:
        jsonpickle.set_preferred_backend('json')
        jsonpickle.set_encoder_options('json', ensure_ascii=False)

        logging.debug('Sending messages ...')

        for city in citiesList:
            cityJsonMessage = jsonpickle.dumps(city, unpicklable=False)
            response = senderService.send_message(QueueUrl=os.getenv('AWS_SQS_URL'),
                                                  DelaySeconds=10,
                                                  MessageBody=cityJsonMessage,
                                                  MessageAttributes={})

        logging.debug('send message is sucessfuly !!!')

    except Exception as error:
        raise Exception(error)
