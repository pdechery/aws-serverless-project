import pytest
import json
from http import HTTPStatus

import send_message_sqs, send_records_dynamo

def test_post_sqs(mock_api_gateway_event, lambda_context):
	event = mock_api_gateway_event()
	result = send_message_sqs.handler(event=event, context=lambda_context)
	assert result == { 'statusCode': HTTPStatus.OK, 'body': 'Message accepted!' }

def test_post_dynamodb(mock_sqs_event, lambda_context):
	data = [
		{'nome': 'Lobisomem', 'song': 'Xou de Bola'},
		{'nome': 'Neto', 'song': 'Nheco nheco'},
	]
	event = mock_sqs_event(json.dumps(data))
	result = send_records_dynamo.handler(event=event, context=lambda_context)
	assert result == { 'statusCode': HTTPStatus.OK, 'body': 'Success' }