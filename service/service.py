import json

def lambda_handler(event, context):
    response = {}
    response["statusCode"]=302
    response["headers"]={'Location': 'https://www.googsle.com'}
    data = {}
    response["body"]=json.dumps(data)
    return response
