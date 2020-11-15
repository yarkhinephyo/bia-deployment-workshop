import json

def lambda_handler(event, context):
    # TODO implement
    
    num1 = event["queryStringParameters"]["num1"]
    num2 = event["queryStringParameters"]["num2"]
    response = {"answer": f"{num1} + {num2} = {num1 + num2}"}
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }