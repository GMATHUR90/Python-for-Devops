import re

input_url = r'/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/Regex_Task_4_Sample_log_containing_dates.txt'
with open(input_url, 'r') as files:
    content = files.read()

print(content)

date_pattern = r'\s*(?P<date>\d{4}-\d{2}-\d{2})'

pattern_match = re.findall(date_pattern,content)

print(pattern_match)

output_url = r'/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/Regex_Task_4_Output.txt'

with open(output_url, 'w') as file_write:
    file_output = '\n'.join(pattern_match)
    file_write.write(file_output)


