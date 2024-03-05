import boto3
import os
import sys
import json
from datetime import datetime

module_path = ".."
sys.path.append(os.path.abspath(module_path))

from utils import bedrock, print_ww

os.environ["AWS_DEFAULT_REGION"] = "us-east-1"
os.environ["BEDROCK_ASSUME_ROLE"] = "arn:aws:iam::122594109988:role/ibm-workshop-emea-virtual"

boto3_bedrock = bedrock.get_bedrock_client(
    assumed_role=os.environ.get("BEDROCK_ASSUME_ROLE", None),
    region=os.environ.get("AWS_DEFAULT_REGION", None),
)

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

    # Summarize the content using Bedrock
    body = json.dumps({
        "prompt": content,
        "max_gen_len": 512,
        "temperature": 0.2,
        "top_p": 0.9
    })

    modelId = 'meta.llama2-13b-chat-v1'
    accept = 'application/json'
    contentType = 'application/json'

    response = boto3_bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read().decode('utf-8'))

    summary = response_body.get('generation')

    # Save the summary to the S3 bucket inside the "summary" directory with a timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    summary_key = f'summary/summary_{timestamp}.txt'
    s3.put_object(Bucket=bucket_name, Key=summary_key, Body=summary)

    # Return the summary
    return summary
