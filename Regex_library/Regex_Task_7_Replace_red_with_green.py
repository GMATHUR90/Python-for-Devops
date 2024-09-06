import re
# Input file patht
input_file_path = r'/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/Regex_Task_7_Sample_log.txt'

with open(input_file_path, 'r') as file:
    log_content = file.read()
# Print the original content of the file
print("Original Content:\n", log_content)

# Define the pattern to search and replacement text
search_pattern = 'red'
replacement_text = 'green'

# Replace occurrences of the pattern in the content    
modified_content = re.sub(search_pattern, replacement_text, log_content)

# Print the modified content
print("Modified Content:\n",modified_content)

# Define the output file path
output_file_path = r'/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/Regex_Task_7_Output.txt'

# Write the modified content to the output file
with open(output_file_path, 'w') as output_file:
    write_output = output_file.write(modified_content)
