import os

# Specify the path to a file
file_path = r'/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/Exception_Handling.py'

# Check if the path exists
if os.path.exists(file_path):
    # Check if it's a file
    if os.path.isfile(file_path):
        print(f"{file_path} exists and is a file.")
    # Check if it's a directory
    elif os.path.isdir(file_path):
        print(f"{file_path} exists and is a directory.")
else:
    print(f"The path {file_path} does not exist.")

"""
O/P:
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents$ /home/gauravmtwt1/Documents/git-demo/.venv/bin/python "/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/OS_Task_1_Check_if_file_Exists.py"
/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/Exception_Handling.py exists and is a file.
"""