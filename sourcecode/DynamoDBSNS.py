import json
import boto3
client = boto3.client('sns')

def DynamoDBSNS_handler(event, context):
    # TODO implement
    topic_arn='arn:aws:sns:us-east-2:411658317626:larryDynamoDB'
    message='Someone is trying to update your table in DynamoDB'
    subject='DynamoDB'
    client.publish(TopicArn=topic_arn,Message=message,Subject=subject)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
