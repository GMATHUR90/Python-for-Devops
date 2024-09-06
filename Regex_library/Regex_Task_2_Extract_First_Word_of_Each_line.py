import re

url = r'Python for DevOps/github_python_topic_upload/Python-for-Devops/Regex_Task_2_logs.txt'

# Reading the input file
with open(url,'r') as file:
    content = file.read()

# Debug: Print the file content
print("File content \n", content)

# Regulare expression to extract the first word of each line
pattern_match = r'^\s*\w+' # This pattern allows for leading whitespaces
    
# Using re.findall with the MULTILINE flag
response = re.findall(pattern_match,content, re.MULTILINE)

print("Extract first word of each line: ", response)

# Output file path
output_url = r'Python for DevOps/github_python_topic_upload/Python-for-Devops/Regex_Task_2_Output.txt'

# Writitng the extracted words to the output file
with open(output_url,'w') as file_write:
    #Convert list to a string with each word on the line
    response_output = '\n'.join(response)
    file_write.write(response_output)

print("Output written to file: ", output_url)

# The pattern ^\s*(\w+) will match the first word of each line, even if there 
# is leading whitespace. The \s* matches zero or more whitespace characters, 
# and (\w+) captures the first word.