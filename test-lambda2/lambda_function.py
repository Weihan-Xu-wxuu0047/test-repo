import json

def lambda_handler(event, context):
    print("1234")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
