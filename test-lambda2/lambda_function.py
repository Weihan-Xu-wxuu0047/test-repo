import json

def lambda_handler(event, context):
    print("from branch2")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
