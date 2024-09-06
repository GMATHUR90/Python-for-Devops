# Access Control List(ACL) of an S3 returns ACL including details about the owner
# and any grants have been set on the bucket.

import boto3

client = boto3.client('s3', region_name='us-east-1')

response = client.get_bucket_acl(
    Bucket = 'gaurav-demo-boto3'
)
print(response)

"""
O/P:
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents$ /home/gauravmtwt1/Documents/git-demo/.venv/bin/python "/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/Python_Task-2_Get_Bucket_ACL_using_Boto3.py"
{'ResponseMetadata': {'RequestId': 'J3TW5QA7675746QT', 'HostId': '3QGlheI8t/1hhgTsTYrtxIOqK90eMnFuo0qpp59gPbimlnAWDLlh0dqw5q20cqGBEck1dudnSMA=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': '3QGlheI8t/1hhgTsTYrtxIOqK90eMnFuo0qpp59gPbimlnAWDLlh0dqw5q20cqGBEck1dudnSMA=', 'x-amz-request-id': 'J3TW5QA7675746QT', 'date': 'Tue, 20 Aug 2024 01:36:21 GMT', 'content-type': 'application/xml', 'transfer-encoding': 'chunked', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'Owner': {'DisplayName': 'kaml-prod-20', 'ID': 'a2ccc51ed9c3b9a070808cb67c36688f3a30e79a7629d07d4c1f148b5cf17bbb'}, 'Grants': [{'Grantee': {'DisplayName': 'kaml-prod-20', 'ID': 'a2ccc51ed9c3b9a070808cb67c36688f3a30e79a7629d07d4c1f148b5cf17bbb', 'Type': 'CanonicalUser'}, 'Permission': 'FULL_CONTROL'}]}
"""