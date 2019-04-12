import os
import json
import requests

def lambda_handler(event, context):
    for item in event['Records']:
        post_slack(item)

def post_slack(item):
    subject = item['Sns']['Subject']
    message = json.loads(item['Sns']['Message'])
    message_id = item['Sns']['MessageId']
    timestamp = item['Sns']['Timestamp']

    pretext = f'【Subject】{subject}\n'
    pretext += f'【Timestamp】{timestamp}\n'
    pretext += f'【MessageId】{message_id}'
    pretext += f'【Message】\n```{json.dumps(message, indent=2)}```\n'

    # https://api.slack.com/incoming-webhooks
    # https://api.slack.com/docs/message-formatting
    # https://api.slack.com/docs/messages/builder
    payload = {
        'attachments': [
            {
                'color': '#e597b2',
                'pretext': pretext,
                #'text': f'```{json.dumps(item, indent=2)}```'
            }
        ]
    }

    # http://requests-docs-ja.readthedocs.io/en/latest/user/quickstart/
    try:
        response = requests.post(os.getenv('SLACK_WEBHOOK_URL'), data=json.dumps(payload))
    except requests.exceptions.RequestException as e:
        print(e)
    else:
        print(response.status_code)
