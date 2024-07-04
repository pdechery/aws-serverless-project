import json
import logging
import os
import uuid
from http import HTTPStatus

import boto3

from collections import namedtuple

logger = logging.getLogger()
logger.setLevel(logging.INFO)

QUEUE_URL = os.getenv('QUEUE_URL')
SQS = boto3.client('sqs')

def handler(event, context):
    '''
    Create SQS Messages
    '''

    message_attrs = {
        'project': {'StringValue': 'Artistas do Brasil', 'DataType': 'String'}
    }

    Song = namedtuple('Song', ['autor', 'titulo'])

    songs = [
        Song('Tom Jobim','Wave'),
        Song('Milton Nascimento','Maria Maria'),
        Song('Tom Jobim','Wave'),
        Song('Pierre Dechery','Dias Atrás'),
        Song('Urutanga','Arara'),
        Song('Lobisomem','Xou de Bola')
    ]

    for song in songs:
        songs_queue = []
        logger.info(song)
        msg_body = {'name': song.autor, 'song': song.titulo}
        songs_queue.append({
            'Id': str(uuid.uuid4()),
            'MessageBody': json.dumps(msg_body),
            'MessageAttributes': message_attrs
        })

    try:
        SQS.send_message_batch(
            QueueUrl=QUEUE_URL,
            Entries=songs_queue
        )
        message = 'Message accepted!'
    except Exception as e:
        logger.exception('Sending message to SQS queue failed!')
        message = str(e)
        status_code = HTTPStatus.INTERNAL_SERVER_ERROR

    return {'statusCode': HTTPStatus.OK, 'body': message}

