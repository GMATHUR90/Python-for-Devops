import re

url = r'Python for DevOps/github_python_topic_upload/Python-for-Devops/Regex_Task_3_Sample_log_Containing_IP_Addresses'

# Reading the file content
with open(url,'r') as file:
    content = file.read()

#print(content)
# Define the regex content to match IP Addresses
ip_pattern = r'\s*(?P<IP_Address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

# Find all matches in the content
match = re.findall(ip_pattern, content)

# Create the string to be written to the output file
ip_extraction_output = "Extracting IP Matches:\n " + '\n'.join(match)

# Output file path
output_url = r'Python for DevOps/github_python_topic_upload/Python-for-Devops/Regex_Task_3_Extract_All_the_IP_Addresses_Output.txt'

# Wrtiing the IP Addresses to the Output file
with open(output_url,'w') as file_output:
    file_output.write(ip_extraction_output)

print("Location of output file: ", output_url)


