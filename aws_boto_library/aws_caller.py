import boto3
from aws_wrapper import show_buckets,upload_files,list_files,create_bucket
s3_obj =  boto3.resource('s3')
 
file_path = '/home/gauravmtwt1/Documents/Python for DevOps/Class9_Final_Project/my_text_file_upload.txt'
show_buckets(s3_obj)
upload_files(s3_obj,'aws-wrapper-s3-bucket',file_path,'my_text_file_upload.txt')
list_files(s3_obj,'aws-wrapper-s3-bucket')    
create_bucket(s3_obj,'aws-wrapper-s3-bucket11')