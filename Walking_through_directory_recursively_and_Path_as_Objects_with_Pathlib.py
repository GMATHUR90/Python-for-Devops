#Walking through directory recursively
# Recursively walk through directories and print details about each file, including 
# last access time and size.

#pip3 install fire

#!/usr/bin/env python
import fire
import os

def walk_path(parent_path):
    print(f"Checking: {parent_path}")
    childs = os.listdir(parent_path)
    for child in childs:
        child_path = os.path.join(parent_path,child)
        if os.path.isfile(child_path):
            last_access = os.path.getatime(child_path)
            size = os.path.getsize(child_path)
            print(f"File: {child_path}")
            print(f"\tlast accessed: {last_access}")
            print(f"\tsize: {size}")
        elif os.path.isdir(child_path):
            walk_path(child_path)
if __name__ == '__main__':
    fire.Fire(walk_path)

"""
O/P: (.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ python Practice.py /home/gauravmtwt1/Documents/webap
p
Checking: /home/gauravmtwt1/Documents/webapp
File: /home/gauravmtwt1/Documents/webapp/app.js
        last accessed: 1710469785.2373552
        size: 0
File: /home/gauravmtwt1/Documents/webapp/index.html
        last accessed: 1710470297.1558409
        size: 0
File: /home/gauravmtwt1/Documents/webapp/backup- 2024-03-14.zip
        last accessed: 1710384298.687181
        size: 799
File: /home/gauravmtwt1/Documents/webapp/Backup.ps1
        last accessed: 1710469389.7130773
        size: 0
File: /home/gauravmtwt1/Documents/webapp/backup- 2024-29-13.zip
        last accessed: 1710470429.6553044
        size: 416
File: /home/gauravmtwt1/Documents/webapp/backup- 2024-03-15.zip
        last accessed: 1710470499.483215
        size: 2435
"""
#Walking Directory Tree using os.walk

import fire
import os

def walk_path(parent_path):
    for parent_path, directories, files in os.walk(parent_path):
        print(f"Checking: {parent_path}")
        for file_name in files:
            file_path = os.path.join(parent_path, file_name)
            last_access =  os.path.getatime(file_path)
            size = os.path.getsize(file_path)
            print(f"File: {file_path}")
            print(f"\tlast accessed: {last_access}")
            print(f"\tsize: {size}")

if __name__ == '__main__':
    fire.Fire(walk_path)

"""
O/P:
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ python Practice.py /home/gauravmtwt1/Documents/webapp
Checking: /home/gauravmtwt1/Documents/webapp
File: /home/gauravmtwt1/Documents/webapp/app.js
        last accessed: 1710469785.2373552
        size: 0
File: /home/gauravmtwt1/Documents/webapp/index.html
        last accessed: 1710470297.1558409
        size: 0
File: /home/gauravmtwt1/Documents/webapp/backup- 2024-03-14.zip
        last accessed: 1710384298.687181
        size: 799
File: /home/gauravmtwt1/Documents/webapp/Backup.ps1
        last accessed: 1710469389.7130773
        size: 0
File: /home/gauravmtwt1/Documents/webapp/backup- 2024-29-13.zip
        last accessed: 1710470429.6553044
        size: 416
File: /home/gauravmtwt1/Documents/webapp/backup- 2024-03-15.zip
        last accessed: 1710470499.483215
        size: 2435
"""

#Path as Objects with Pathlib

# re-write find_rc

import os
import pathlib

def find_rc(rc_name=".config/google-chrome"):
    #Check for Env variable
    var_name = "EXAMPLERC_DIR"
    example_dir = os.environ.get(var_name)
    if example_dir:
        dir_path = pathlib.Path(example_dir)
        config_path = dir_path / rc_name
        print(f"Checking {config_path}")
        if config_path.exists():
            return config_path.as_posix()
        
# Check the current working directory

    config_path = pathlib.Path.cwd() / rc_name
    print(f"Checking {config_path}")
    if config_path.exists():
        return config_path.as_posix()
    
# Check user home directory
   
    config_path = pathlib.Path.home() / rc_name
    print(f"Checking {config_path}")
    if config_path.exists():
        return config_path.as_posix()
    
# Check directory of this file
    file_path = pathlib.Path(__file__) .resolve()
    parent_path = file_path.parent
    config_path =  parent_path / rc_name
    print(f"Checking {config_path}")
    if config_path.exists():
        return config_path.as_posix()

    print(f"File {rc_name} has not been found")
        
# Example is usage
if __name__ == '__main__':
    config_file =  find_rc()
    if config_file:
        print(f"Configuration file found : {config_file}")
    else:
        print("No configuration file found.")

"""
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ /home/gauravmtwt1/Documents/git-demo/.venv/bin/python "/home/gauravmtwt1/Documents/Python for DevOps/revision_python09feb2024onward.py"
Checking /home/gauravmtwt1/Documents/Python for DevOps/.config/google-chrome
Checking /home/gauravmtwt1/.config/google-chrome
Configuration file found : /home/gauravmtwt1/.config/google-chrome
"""

