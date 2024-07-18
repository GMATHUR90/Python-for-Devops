#Managing Files and Directories using os.path

#os.path allows user to create,manipulate, and navigate file system paths in a cross-platform
#manner

#Key method for Path Manipulation

#1. Getting the Current Working Directory

import os

cur_dir = os.getcwd()
print("Current Directory",cur_dir)

"""
O/P:Current Directory /home/gauravmtwt1/Documents
"""

#2. Splitting Path

head_tail = os.path.split(cur_dir)
print(head_tail)
"""
O/P:('/home/gauravmtwt1', 'Documents')
"""

#3.Getting the Directory Name

parent_dir = os.path.dirname(cur_dir)
print(parent_dir)

"""
O/P:/home/gauravmtwt1
"""

#4.Getting the base name
leaf_name = os.path.basename(cur_dir)
print(leaf_name)

"""
O/P:Documents
"""

#5.Walking up a Directory Tree
# To travel up the directory tree using 'os.path.dirname'

while os.path.basename(cur_dir):
    cur_dir = os.path.dirname(cur_dir)
    print(cur_dir)

"""
O/P:(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents$ /home/gauravmtwt1/Documents/git-demo/.venv/bin/python "/home/gauravmtwt1/Documents/Python for DevOps/revision_python09feb2024onward.py"
/home/gauravmtwt1
/home
/
"""
#This loop will keep printing the parent directory until it reaches the root.


#Example for locating an RC File

#In Unix-like systems,configuration files(rc files) are commonly used to set up application
# configuration.

import os

def find_rc_file():
    rc_file = '.myapprc'
    locations = [
        os.path.join(os.getcwd(),rc_file) ,# Check current working directory
        os.path.join(os.path.expanduser('~'), rc_file) #Check user's home directory
    ]
# Check if an environment variable is set for rc file location
    env_rc_file = os.getenv('MYAPPRC') # retrieve an environment variable
    if env_rc_file:
        locations.insert(0, env_rc_file) #0 here stand for index'0' of locations list.

    for location in locations:
        if os.path.exists(location):
            return location
        
    return None

rc_path = find_rc_file()
if rc_path:
    print(f"RC file found at:  {rc_path}")
else:
    print("RC file not found")

"""
O/P:(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents$ /home/gauravmtwt1/Documents/git-demo/.venv/bin/python "/home/gauravmtwt1/Documents/Python for DevOps/revision_python09feb2024onward.py"
RC file not found
"""

#The function first checks an environment variable for the rc file location, then the
# current working directory, and finally the user's home directory. It returns the path
# to the rc file if found, otherwise returns 'None'.

#Example for locating VS code setting file in ubuntu

import os

def find_vscode_settings():
    #Define the common locations for VS Code settings on Linux
    setting_file = 'settings.json'
    locations = [
        os.path.join(os.path.expanduser('~'),'.config','Code','User',setting_file),#Standard VS Code Setting
        os.path.join(os.path.expanduser('~'),'.vscode',setting_file) #Possible workspace-specific settings

    ]

    #Check if an environment variable is set for the VS code settings file location
    env_vscode_settings = os.getenv('VSCODE_SETTINGS')
    if env_vscode_settings:
        locations.insert(0,env_vscode_settings)
    
    for location in locations:
        if os.path.exists(location):
            return location
    return None
vscode_settings_path = find_vscode_settings()
if vscode_settings_path:
    print(f"VS Code settings file found at: {vscode_settings_path}")
else:
    print("VS Code setting file not found")

"""
O/P: VS Code settings file found at: /home/gauravmtwt1/.config/Code/User/settings.json
"""