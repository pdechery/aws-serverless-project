import json
import logging
import os

import boto3

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
