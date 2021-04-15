from __future__ import print_function
import boto3
import base64
import json

eventbridge_client = boto3.client('events')
# Include your SNS topic ARN here.
#topic_arn = 'arn:aws:sns:<region>:<account_id>:<topic_name>'


def lambda_handler(event, context):
    output = []
    success = 0
    failure = 0
    print("DEBUG: event: {}".format(event))
    for record in event['records']:
        # Uncomment the below line to publish the decoded data to the SNS topic.
        payload = base64.b64decode(record['data'])
        print("DEBUG: payload: {}".format(payload))
        response = _send_to_eventbridge(payload)
        print("DEBUG: response: {}".format(response))
        #client.publish(TopicArn=topic_arn, Message=payload, Subject='Sent from Kinesis Analytics')
        output.append(response)
    print(output)
    return {'records': output}

def _send_to_eventbridge(payload):
    print("DEBUG: detail: {}".format(json.dumps(payload)))
    entries=[
        {
            'Detail': "{}".format(payload),
            "DetailType": "blkinesisevent",
            'EventBusName': 'arn:aws:events:eu-west-1:394348467270:event-bus/BLKinesis',
            'Source': 'internal.pipeline.blevents'
        }
        ]
    response = eventbridge_client.put_events(Entries=entries)

    return response