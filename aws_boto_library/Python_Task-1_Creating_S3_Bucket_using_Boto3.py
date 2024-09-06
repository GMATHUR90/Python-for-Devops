# Login to your aws account using 'aws configure" command by providing access keys.
# pip install boto3

#Task1 : Create S3 bucket

import boto3

client = boto3.client('s3', region_name='us-east-1')

response = client.create_bucket(
    
    Bucket='gaurav-demo-boto3',
    
)
print(response)

"""
O/P: (.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents$ /home/gauravmtwt1/Documents/git-demo/.venv/bin/python "/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/Python_Tasks_for_Devops_File_Operation_and_Boto3.py"
{'ResponseMetadata': {'RequestId': 'G700WB94J2MK991Q', 'HostId': 'FUCBgDFnCZWlWETvxaWPJ7yTj4QvST77sTo1ds5TH7zaDtR3oP0SQnfVIY6zJhBCCzGIOc3FG6YJ91RtXW+oFcJRIRtABXFIyL61xn9YbAs=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'FUCBgDFnCZWlWETvxaWPJ7yTj4QvST77sTo1ds5TH7zaDtR3oP0SQnfVIY6zJhBCCzGIOc3FG6YJ91RtXW+oFcJRIRtABXFIyL61xn9YbAs=', 'x-amz-request-id': 'G700WB94J2MK991Q', 'date': 'Mon, 19 Aug 2024 02:03:45 GMT', 'location': '/gaurav-demo-boto3', 'server': 'AmazonS3', 'content-length': '0'}, 'RetryAttempts': 0}, 'Location': '/gaurav-demo-boto3'}

"""
 

