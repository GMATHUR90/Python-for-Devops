import re
# Input file path
input_url = r'/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/Regex_5_Sample_log.txt'
# Read the content of the file
with open(input_url, 'r') as file:
    content = file.read()
# Print the content of the file
print(content)

# Regular expression pattern to match most addresses
#email_addr_pattern = '\s*(?P<Email>\w+\.\w+@\w+\.\w+)'

email_addr_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

# Find all matching addresses
matches = re.findall(email_addr_pattern,content)
# Output file path
output_url = r'/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/Regex_5_Output.txt'
# Write the matches to the output file
with open(output_url, 'w') as file_output:
    output = '\n'.join(matches)
    file_output.write(output)