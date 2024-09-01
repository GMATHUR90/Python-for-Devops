import re

input_file_path = r'/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/Regex_Task_8_Sample_log.txt'

with open(input_file_path , 'r') as file:
    content = file.read()
#print(content)

output_file_path = r'/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/Regex_Task_8_Output.txt'

# Task-1 Replace tabs with four spaces
content_with_tab= content.replace('\\t','\t')

tab_pattern = '\t'

space_replaced_tab = ' '

content_with_spaces = re.sub(tab_pattern, space_replaced_tab , content_with_tab)

with open(output_file_path ,'w') as file_1:
    file_1.write("Task-1: Replacing tabs with spaces:\n ")
    file_1.write(content_with_spaces + "\n\n")

# Task-2 Extract all number

number_pattern = r'(\d+)'

numbers_found = re.findall(number_pattern , content_with_spaces)

with open(output_file_path, 'a') as file_2:
    
    file_2.write("Task-2: Extracted all number from logs:\n")
    file_2.write("\n".join(numbers_found) + "\n\n")

# Task-3 Extract first word for each line
first_word_pattern = r'^\s*(\w+)'

first_words = re.findall(first_word_pattern, content_with_spaces, re.MULTILINE)
with open(output_file_path, 'a') as file_3:
    file_3.write("Task-3: Extracted first words of each line:\n")
    file_3.write("\n".join(first_words) + "\n\n")
 
# Task-4 Extract all IP Address
ip_pattern = r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3})'
ip_addresses = re.findall(ip_pattern,content_with_spaces)
print("Extracted IP Pattern \n: ",ip_addresses)

with open(output_file_path,'a') as file_4:
    file_4.write("Task-4: Extracted IP Addresses:\n")
    file_4.write("\n".join(ip_addresses) + "\n\n")

# Task-5 Extract dates in the format yyyy-mm-dd

date_pattern = r'\[(?P<date>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]'  
dates_found = re.findall(date_pattern,content_with_spaces) 

with open(output_file_path, 'a') as file_5:
    file_5.write("Task-5: Extracted dates:\n")
    file_5.write("\n".join(dates_found) + "\n\n")

# Task-6 Extract Email Address

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z.-]+\.[A-Za-z]{2,}\b'
email_found = re.findall(email_pattern,content)

with open(output_file_path, 'a') as file_6:
    file_6.write("Task-6: Extracted email addresses:\n")
    file_6.write("\n".join(email_found) + "\n\n")

# Task-7 Replace red with green

content_with_green = re.sub(r'\bred\b','green',content_with_spaces,flags=re.IGNORECASE)

with open(output_file_path, 'a') as file_7:
    file_7.write("Task-7: Replaced 'red' with 'green' and 'RED' with 'GREEN':\n")
    file_7.write(content_with_green)


