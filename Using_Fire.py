#!/usr/bin/env python
#Using Fire Package

# fire package provides a way to create CLI with minimal code.
# It uses introspection to generate the interface automatically based on the functions
# and arguments you define.

#Simple Fire example

import fire

def greet(greeting='Hiya', name='Tammy'):
    print(f"{greeting} {name}")

def goodbye(goodbye='Bye', name='Tammy'):
    print(f"{goodbye} {name}")
if __name__ == '__main__':
    fire.Fire()

"""
O/P: NAME
    Using_Fire.py

SYNOPSIS
    Using_Fire.py GROUP | COMMAND

GROUPS
    GROUP is one of the following:

     fire
       The Python Fire module.

COMMANDS
    COMMAND is one of the following:

     greet

     goodbye

(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload$ ./Using_Fire.py greet --greeting "Hello" --name "Gaurav"
Hello Gaurav

(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload$ ./Using_Fire.py goodbye --goodbye "Farewell" --name "Gaurav"
Farewell Gaurav
"""

#Nested CLI using Fire Package

#!/usr/bin/env python
# Command-line tool using fire

import fire

class Ships:
    def sail(self):
        ship_name = 'Your ship'
        print(f"{ship_name} is setting sail")
    
    def list(self):
        ships = ['John B', 'Yankee Clipper', 'Pequod']
        print(f"Ships: {', '.join(ships)}")

def sailors(greeting, name):
    message = f'{greeting} {name}'
    print(message)

class Cli:
    def __init__(self):
        self.sailors = sailors
        self.ships = Ships()

if __name__ == '__main__':
    fire.Fire(Cli)

"""
O/P: NAME
    Using_Fire.py

SYNOPSIS
    Using_Fire.py GROUP | COMMAND

GROUPS
    GROUP is one of the following:

     ships

COMMANDS
    COMMAND is one of the following:

     sailors
"""
"""

NAME
    Using_Fire.py ships

SYNOPSIS
    Using_Fire.py ships COMMAND

COMMANDS
    COMMAND is one of the following:

     list

     sail
"""
"""
NAME
    Using_Fire.py sailors

SYNOPSIS
    Using_Fire.py sailors GREETING NAME

POSITIONAL ARGUMENTS
    GREETING
    NAME

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS     

"""
"""
1. Set Sail

(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload$ ./Using_Fire.py ships sail
Your ship is setting sail

2. List Ships

(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload$ ./Using_Fire.py ships list
Ships: John B, Yankee Clipper, Pequod

3. Greet Sailor

(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload$ ./Using_Fire.py sailors --greeting Hello --name Gaurav
Hello Gaurav

"""
#Interactive Mode

"""
O/P:
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload$ ./Using_Fire.py sailors Hiya Gaurav -- --interactive
Hiya Gaurav
Fire is starting a Python REPL with the following objects:
Modules: fire
Objects: Cli, Ships, Using_Fire.py, component, result, sailors, self, trace

Python 3.10.12 (main, Mar 22 2024, 16:50:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
"""