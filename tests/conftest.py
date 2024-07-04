import pytest


@pytest.fixture()
def lambda_context():
	class MockLambdaContext():
		invoked_function_arn = "arn:aws:lambda:us-east-1:957452081947:function:aws-projects-dev-producer"

	return MockLambdaContext()


@pytest.fixture()
def mock_api_gateway_event():
  def wrapper():
    return {
      "version": "2.0",
      "routeKey": "GET /send_message_sqs",
      "requestContext": {
          "http": {
              "method": "GET",
              "path": "/send_message_sqs",
          },
      }
    }

  return wrapper


@pytest.fixture()
def mock_sqs_event():
  def wrapper(data):
    return {
      "Records": [
          {
            "body": data,
            "messageAttributes": {
              "project": {
                "stringValue": "Artistas do Brasil"
              }
            }
          }
        ]
      }

  return wrapper

