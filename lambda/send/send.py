import boto3 
import os
import json
from datetime import datetime

def lambda_handler(event, context):
    sqs = boto3.client('sqs')
    now = datetime.now() 
    current = now.strftime("%H:%M:%S") 
     
    sqs.send_message(
        QueueUrl = os.environ.get("QUEUEURL"),
        MessageGroupId = '1',
        MessageBody = current)
    return {
        'statusCode': '200',
        'body': json.dumps(current)
    }