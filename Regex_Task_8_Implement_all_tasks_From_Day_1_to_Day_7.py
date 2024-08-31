import re

input_file_path = r'/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/Regex_Task_8_Sample_log.txt'

with open(input_file_path , 'r') as file:
    content = file.read()
#print(content)

output_file_path = r'/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/Regex_Task_8_Output.txt'

content_with_tab= content.replace('\\t','\t')

tab_pattern = '\t'

space_replaced_tab = ' '

tab_match = re.sub(tab_pattern, space_replaced_tab , content_with_tab)

with open(output_file_path ,'w') as file_1:
    print("Final Output replacing tabs with spaces : ")
    file_1.write(tab_match)

# Task-2 Extract all number
print()
number_pattern = r'(\d+)'

number_pattern_output = re.findall(number_pattern , content_with_tab)
#print(number_pattern_output)

with open(output_file_path, 'a') as file_2:
    file_2_output = "\n".join(number_pattern_output) 
    print("Task-2: Extracted numbers from logs: ")
    file_2.write(file_2_output)

# Task-3
word_pattern = r'^\s*(\w+)'

word_pattern_output = re.findall(word_pattern, tab_match, re.MULTILINE)
print("Extract first word of each line: ", word_pattern_output)

with open(output_file_path, 'a') as file_3:
    for word in word_pattern_output:
        file_3.write( '\n' + word)
