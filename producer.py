import json
import logging
import os
import uuid

import boto3

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

QUEUE_URL = os.getenv('QUEUE_URL')
SQS = boto3.client('sqs')


def handler(event, context):
    '''
    Create SQS Messages
    '''
    status_code = 200
    message = ''

    logger.debug(event)

    if not event.get('body'):
        return {'statusCode': 400, 'body': json.dumps({'message': 'No body was found'})}

    try:
        message_attrs = {
            'project': {'StringValue': 'Artistas do Brasil', 'DataType': 'String'}
        }
        SQS.send_message_batch(
            QueueUrl=QUEUE_URL,
            Entries=[
                {
                    'Id':str(uuid.uuid4()),
                    'MessageBody':"{'nome': 'Tom Jobim', 'song': 'Wave'}",
                    'MessageAttributes':message_attrs,
                },
                {
                    'Id':str(uuid.uuid4()),
                    'MessageBody':"{'nome': 'Milton Nascimento', 'song': 'Maria Maria'}",
                    'MessageAttributes':message_attrs,
                },
                {
                    'Id':str(uuid.uuid4()),
                    'MessageBody':"{'nome': 'Pierre Dechery', 'song': 'Dias Atrás'}",
                    'MessageAttributes':message_attrs,
                },
                {
                    'Id':str(uuid.uuid4()),
                    'MessageBody':"{'nome': 'Urutanga', 'song': 'Arara'}",
                    'MessageAttributes':message_attrs,
                },
                {
                    'Id':str(uuid.uuid4()),
                    'MessageBody':"{'nome': 'Lobisomem', 'song': 'Xou de Bola'}",
                    'MessageAttributes':message_attrs,
                }
            ]
        )
        message = 'Message accepted!'
    except Exception as e:
        logger.exception('Sending message to SQS queue failed!')
        message = str(e)
        status_code = 500

    return {'statusCode': status_code, 'body': json.dumps({'message': message})}

