import json
import logging
import os

import boto3
import botocore

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def handler(event, context):
    '''
    Send records to DynamoDB
    '''

    logger.debug(event)
    
    for record in event['Records']:
        logger.info(f'Message body: {record["body"]}')
        logger.info(
            f'Message attribute: {record}'
        )

    dynamodb = boto3.client('dynamodb')

    try:
        response = dynamodb.put_item(
            TableName="artists",
            Item={
                'name':{
                    'S':'Beto Guedes'
                },
                'song':{
                    'S':'Amor de Índio'
                },
                'album_info':{
                    'M':{'nome':{'S':'Amor de Índio'},'ano':{'N':'1975'}}
                },
                'letra':{
                    'S':'https://www.google.com/search?q=beto+guedes+amor+de+%C3%ADndio&rlz=1C1VDKB_pt-PTBR1089BR1089&oq=beto+guedes+amor+de+%C3%ADndio&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQLhiABDIHCAIQABiABDIICAMQABgWGB4yCAgEEAAYFhgeMggIBRAAGBYYHjIICAYQABgWGB4yCAgHEAAYFhgeMggICBAAGBYYHjIICAkQABgWGB7SAQg0OTA2ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8#wptab=si:ALGXSlaqmEzXP-BTuaSuCvblodZyXkKSMAGRjFsw0n3X-lbdEvbZMF4ZCYtDeZbJCsoWygGeDZ1i5-Lo-xqrb8_tmYu_rebH7AvDB0_-jBrZG1vH3EP80e4VVK91HGa8wRhWKvSm-Re8xhgKcV-_Rp8fWyUajFMRrsoi2pwMKOy0GDMaHvH8B6U%3D'
                }
            },
            ExpressionAttributeNames={
                '#N':'name'
            },
            ConditionExpression='attribute_not_exists(#N) AND attribute_not_exists(song)',
            ReturnConsumedCapacity='TOTAL'
        )
        print(response)
    except botocore.exceptions.ClientError as error:
        print(error)
