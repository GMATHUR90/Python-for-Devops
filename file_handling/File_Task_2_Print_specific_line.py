#Tasks:
# 1. Print first line
# 2. Print last line
# 3. Print 12th line

input_file_path = r'/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/File_Task_2_Sample_logs.txt'
with open(input_file_path, 'r') as file:
    content = file.readlines()
#print(content)
print(content[0])
print(content[11])

print(content[-1])

output_file_path = r'/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/File_Task_2_Output.txt'
with open(output_file_path, 'w') as file_output:
    file_output.write(f"This is line_1: {content[0]}\n")
    file_output.write(f"This is line_12: {content[11]}\n")
    file_output.write(f"This is last line: {content[-1]}\n")