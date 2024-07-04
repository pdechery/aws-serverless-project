import json
import logging
import os
import boto3

from http import HTTPStatus
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    '''
    Send records to DynamoDB
    '''

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('artists')

    songs = [
      {
        "artist": "Pierre Dechery",
        "song": "Assim Será",
        "info": {
          "arranjo": ["Guitarra","Baixo","Bateria"],
          "data-gravacao": "2023-09-02T00:00:00Z",
          "estilos": [
            "Rock",
            "Grungy",
            "Guitar"
          ],
          "descricao": "Uma música bem antiga que sempre gostei"
        }
      },
      {
      "artist": "Pierre Dechery",
      "song": "Parará",
      "info": {
        "arranjo": ["Guitarra","Baixo","Bateria"],
        "data-gravacao": "2023-11-02T00:00:00Z",
        "estilos": [
          "Pop",
          "Anos 80"
        ],
        "descricao": "Uma música nova bem legal"
      },
      "duracao": 300,
      "plataformas": ["Souncloud","YouTube","Spotify"]
      }
    ]

    try:
      with table.batch_writer() as writer:
        for song in songs:
          writer.put_item(Item=song)
    except ClientError as err:
      logger.error(
        "Couldn't load data into table %s. Here's why: %s: %s",
        table.name,
        err.response["Error"]["Code"],
        err.response["Error"]["Message"],
      )

    return {"statusCode":HTTPStatus.OK, "body": "Success"}
