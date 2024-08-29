import re

url = r'/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/Linux.log'

with open(url,'r') as file:
    content = file.read()

number_pattern =r'(\d+)'

match = re.findall(number_pattern,content)

if match:
    print(match)
