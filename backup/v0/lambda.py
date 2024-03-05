import boto3
import os
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
        print(content)

    # You can return or process the content as needed
    return content
