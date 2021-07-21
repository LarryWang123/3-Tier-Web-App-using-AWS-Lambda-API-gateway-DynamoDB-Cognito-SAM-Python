# import the json utility package since we will be working with a JSON object
import json
# import the AWS SDK (for Python the package name is boto3)
import boto3

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('AWSDatabase')


# define the handler function that the Lambda service will use as an entry point
def queryDynamoDB_handler(event, context):
# extract values from the event object we got from the Lambda service and store in a variable
    key = event['queryStringParameters']['topic']
# write name and time to the DynamoDB table using the object we instantiated and save response in a variable
    
    response = table.get_item(Key={'Topic': key})
  

# return a properly formatted JSON object
    return {
#        'statusCode': 200,
        'body': json.dumps(response['Item']['Contents'])
    }
