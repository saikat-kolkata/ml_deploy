import json
import boto3
import ast

def lambda_handler(event, context):
    # TODO implement
    runtime_client = boto3.client('runtime.sagemaker')
    endpoint_name = 'xgboost-2024-07-01-15-15-04-XXX'
    
    # sample = '5.1,3.5,1.4,0.2'
    sample = '{},{},{},{}'.format(ast.literal_eval(event['body'])['x1'],
                                    ast.literal_eval(event['body'])['x2'],
                                    ast.literal_eval(event['body'])['x3'],
                                    ast.literal_eval(event['body'])['x4'])
    
    
    response = runtime_client.invoke_endpoint(EndpointName = endpoint_name,
    ContentType = 'text/csv', Body=sample)
    
    result = int(float(response['Body'].read().decode('ascii')))

    print(result)
    return {
        'statusCode': 200,
        'body': json.dumps({'prediction': result})
    }
