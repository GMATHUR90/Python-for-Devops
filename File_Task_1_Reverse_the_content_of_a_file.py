
#Input File Path
input_file_path = r'/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/File_Task_1_Sample_log.txt'

# Open the input file path in read mode and read its content
with open(input_file_path, 'r') as file:
    file_content = file.read()

# Print the original content of file
print(file_content)

# Reverse the content of the file
reverse_content = file_content[::-1]

# Print the reversed content
print("Reversed Content: \n",reverse_content)

# Outut file path
output_file_path = r'/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/File_Task_1_Output.txt'

# Open the output file in write mode and write the reversed content
with open(output_file_path,'w') as file_output:
    content_output = file_output.write(reverse_content)

print(f"Reversed content has been written to {output_file_path}")