import json

def lambda_handler(event, context):
    print('notify_slack')
    print(json.dumps(event))
