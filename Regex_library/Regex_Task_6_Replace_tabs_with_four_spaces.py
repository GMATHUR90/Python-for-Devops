import re
# Input file path
input_url = r'/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/Regex_Task_6_Sample_logs.txt'

# Read the content of the file

with open(input_url, 'r') as file:
    content = file.read()

print("Original Content: \n ",content)

# Replace string '\t' with an actual tab character '\t'
# This handles cases where the file might have been saved with escaped cases.

content_with_tabs = content.replace('\\t','\t')

print(content_with_tabs)

pattern = '\t'
replacement= '    '

# Replace all tab character in the content with four spaces
new_log = re.sub(pattern, replacement, content_with_tabs)

print()
print("\nModified Content: \n", new_log)

output_url = r'/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/Regex_Task6_Output.txt'

# Write the modified content to the output file
with open(output_url, 'w') as file_output:
    file_output.write(new_log)
print(f"Tabs replaced with spaces and saved to: {output_url}")