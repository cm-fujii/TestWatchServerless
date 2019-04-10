import os
import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('lambda')

    param = {
        'hoge': 'fuga'
    }

    client.invoke(
        FunctionName=os.getenv('TARGET_LAMBDA_FUNCTION'),
        InvocationType='Event',
        Payload=json.dumps(param)
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
