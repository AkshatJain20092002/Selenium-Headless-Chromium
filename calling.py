import json
# from openai_Apikey import open_api
from lambda_function import lambda_handler  # Import the Lambda handler

# Define the event for the Lambda function
event = {
    "requestContext": {
        "http": {
            "method": "POST"
        }
    },
    "path": "/lambda_googlescholar",
    "body": json.dumps({
        "keywords": ["AI"],
        "num_papers": 20
        })
}

# Context (can be empty for now)
context = {}

# Call the Lambda function directly
response = lambda_handler(event, context)

# Print the response
print(response)
