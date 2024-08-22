import boto3

# Initialize a session using Amazon EC2 client
ec2_client = boto3.client('ec2', region_name='us-east-1')

# Create a new key pair
key_pair = ec2_client.create_key_pair(KeyName='Boto3-Ec2-Instance-Created')

# Save the private key to a file(this is important for SSH access)
with open('Boto3-Ec2-Instance-Created','w') as file:
    file.write(key_pair['KeyMaterial'])
print("Key pair created and saved as 'Boto3-Ec2-Instance-Created.pem'")

# Launch a new EC2 instance
response = ec2_client.run_instances(
    ImageId='ami-0e86e20dae9224db8',
    InstanceType='t2.micro',
    KeyName="Boto3-Ec2-Instance-Created",
    SecurityGroupIds=['sg-02ab6c9a15d9a92c9'],
    SubnetId='subnet-06395305d28f3310d',
    MinCount=1,
    MaxCount=1
)
# Output the Instance ID of the newly created instance

instance_id = response['Instances'][0]['InstanceId']
print(f'Instance created with ID: {instance_id}')

"""
O/P: (.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents$ /home/gauravmtwt1/Documents/git-demo/.venv/bin/python "/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/Python_Task-3_Creating_EC2_Instance_Using_Boto3.py"
Key pair created and saved as 'Boto3-Ec2-Instance-Created.pem'
Instance created with ID: i-0e1682773089cb9eb
"""