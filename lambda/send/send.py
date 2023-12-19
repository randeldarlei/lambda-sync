import boto3 
import os
import json
import urllib.parse
from pprint import pprint

def lambda_handler(event, context):

    s3 = boto3.client('s3')

    bucket = event['Records'][0]['s3']['bucket']['name']
    filename = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    file = s3.get_object(Bucket='python-sync', Key='Área de Trabalho/test.json')

    text = file['Body'].read().decode()
    data = json.loads(text)

    print(data)

def send(data):
    
    sqs = boto3.client('sqs')
     
    sqs.send_message(
        QueueUrl = os.environ.get("QUEUEURL"),
        MessageGroupId = '1',
        MessageBody = data)
    return {
        'statusCode': '200',
        'body': json.dumps(data)
    }