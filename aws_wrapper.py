#import boto3

#s3_obj =  boto3.resource('s3') 

def show_buckets(s3_obj):
    for bucket in s3_obj.buckets.all(): #same output as aws s3 ls
        #print(bucket)
        print(bucket.name)
#key_name = s3 file name
#rb = compressed binary formatted data
def upload_files(s3_obj,bucket_name,file_path,key_name):
    file_data = open(file_path,"rb") #open
    s3_obj.Bucket(bucket_name).put_object(Key=key_name,Body=file_data) #processed
    file_data.close()#close
    print("file uploaded successfully") 

def list_files(s3_obj,bucket_name):
    print(f"The file in {bucket_name} are: ")
    for object in s3_obj.Bucket(bucket_name).objects.all():
        print(object.key)
def create_bucket(s3_obj,bucket_name):
    s3_obj.create_bucket(Bucket=bucket_name)
    print(f"bucket{bucket_name} created successfully")
