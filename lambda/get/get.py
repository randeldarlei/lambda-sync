import boto3
import os

def lambda_handler(event, context):
    sqs = boto3.client('sqs')
    response = sqs.receive_message(
        queueurl='https://sqs.us-east-1.amazonaws.com/915531505420/lambda-sync.fifo',
        AttributeNames=[
        'All',
        'Policy',
        'VisibilityTimeout',
        'MaximumMessageSize',
        'MessageRetentionPeriod',
        'ApproximateNumberOfMessages',
        'ApproximateNumberOfMessagesNotVisible',
        'CreatedTimestamp',
        'LastModifiedTimestamp',
        'QueueArn',
        'ApproximateNumberOfMessagesDelayed',
        'DelaySeconds',
        'ReceiveMessageWaitTimeSeconds',
        'RedrivePolicy',
        'FifoQueue',
        'ContentBasedDeduplication',
        'KmsMasterKeyId',
        'KmsDataKeyReusePeriodSeconds',
        'DeduplicationScope',
        'FifoThroughputLimit',
        'RedriveAllowPolicy',
        'SqsManagedSseEnabled',
    ],
    MessageAttributeNames=[
        'string',
    ],
    MaxNumberOfMessages=123,
    VisibilityTimeout=123,
    WaitTimeSeconds=123,
    ReceiveRequestAttemptId='string'
)
    event = {
        'statusCode': 200,
        'body': response.get('Messages', [])
}
    return event