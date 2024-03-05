import boto3
import os
import json
from datetime import datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'super-team-7-ibm'
    
    # Get the list of objects in the bucket
    objects = s3.list_objects(Bucket=bucket_name)
    
    # Filter .txt files
    txt_files = [obj for obj in objects['Contents'] if obj['Key'].endswith('.txt')]
    
    # Get the latest .txt file
    latest_file = max(txt_files, key=lambda x: x['LastModified'])
    
    # Download the file to the Lambda's temporary directory
    local_path = '/tmp/{}'.format(latest_file['Key'])
    s3.download_file(bucket_name, latest_file['Key'], local_path)
    
    # Read the file
    with open(local_path, 'r') as file:
        content = file.read()

    # Summarize the content using Bedrock API
    api_key = 'YOUR_API_KEY' # Replace with your actual Bedrock API Key
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key
    }
    payload = {
        "prompt": content,
        "max_gen_len": 512,
        "temperature": 0.2,
        "top_p": 0.9
    }
    
    invoke_endpoint_url = 'https://api.openai.com/v1/models/meta.llama2-13b-chat-v1/invoke'
    response = requests.post(invoke_endpoint_url, headers=headers, data=json.dumps(payload))
    response_body = json.loads(response.text)

    summary = response_body.get('generation')

    # Save the summary to the S3 bucket inside the "summary" directory with a timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    summary_key = f'summary/summary_{timestamp}.txt'
    s3.put_object(Bucket=bucket_name, Key=summary_key, Body=summary)

    # Return the summary
    return summary
