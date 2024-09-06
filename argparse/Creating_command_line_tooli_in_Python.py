#Creating command line tool in Python

#Creating command line tools in python involve a few steps to ensure your script behaves
# correctly both when executed directly and when imported as module .

#Basic Structure

#1. Function definition and invocation:
#Define your main functionality within a function and call it only when the script is
# executed.

def say_it():
    greeting = 'Hello'
    target = 'Joe'
    message = f'{greeting} {target}'
    print(message)
if __name__ == '__main__':
    say_it()

#2. Running the script
# You can run the script directly using Python
"""
O/P:
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ python say_it.py
Hello Joe
"""

#3.Making the script Executable:
#Add a shebang('#!/usr/bin/env python') to the top of your script and make it executable.
"""
#!/usr/bin/env python
def say_it():
    greeting = 'Hello'
    target = 'Joe'
    message = f'{greeting} {target}'
    print(message)
if __name__ == '__main__':
    say_it()
"""
#change it execution permission with chmod
"""
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents$ cd Python\ for\ DevOps/
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ ls -la say_it.py 
-rw-rw-r-- 1 gauravmtwt1 gauravmtwt1 173 Jul 22 07:00 say_it.py
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ chmod +x say_it.py 
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ ls -la say_it.py 
-rwxrwxr-x 1 gauravmtwt1 gauravmtwt1 173 Jul 22 07:00 say_it.py
"""

#Now you can run it without explicitly calling Python
"""
O/P: (.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents$ cd Python\ for\ DevOps/
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ ./say_it.py
Hello Joe
"""

#Accepting Command Line Argument
# To make your script more versatile, you can accept command-line arguments using the
# argparse module.

#1. Import 'argparse'

#!/usr/bin/env python
"""
def say_it():
    greeting = 'Hello'
    target = 'Joe'
    message = f'{greeting} {target}'
    print(message)
if __name__ == '__main__':
    say_it()

"""
"""
#!/usr/bin/env python
import argparse

def say_it(greeting, target):
    message = f'{greeting} {target}'
    print(message)
if __name__ == '__main__':
    parser =  argparse.ArgumentParser(description= 'Say hello to someone. ')
    parser.add_argument('--greeting', default='Hello', help='The greeting word')
    parser.add_argument('--target', default='Joe', help='The person to greet')
    args = parser.parse_args()

    say_it(args.greeting, args.target)
"""
"""
O/P: (.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ ./say_it.py --greeting Hi --target Alice
Hi Alice
"""


#More complex example

#!/usr/bin/env python
import argparse

def greet(greeting, target):
    message = f'{greeting} {target}'
    print(message)

def farewell(farewell_message , target):
    message = f'{farewell_message}{target}'
    print(message)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Greet or bid farewell to someone.')
    subparsers = parser.add_subparsers(dest='command')

    greet_parser = subparsers.add_parser('greet', help='Greet someone')
    greet_parser.add_argument('--greeting',default='Hello', help='The greeting word')
    greet_parser.add_argument('--target',default='Goodbye', help='The farewell message')

    args = parser.parse_args()

    if args.command == 'greet':
        greet(args.greeting , args.target)
    elif args.command == 'farewell':
        farewell(args.farewell_message, args.target)


import argparse

def greet(greeting, target):
    message = f'{greeting} {target}'
    print(message)

def farewell(farewell_message , target):
    message = f'{farewell_message} {target}'
    print(message)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Greet or bid farewell to someone.')
    subparsers = parser.add_subparsers(dest='command')

    greet_parser = subparsers.add_parser('greet', help='Greet someone')
    greet_parser.add_argument('--greeting',default='Hello', help='The greeting word')
    greet_parser.add_argument('--target',default='Goodbye', help='The farewell message')

    farewell_parser =  subparsers.add_parser('farewell', help = 'Bid farewell to someone')
    farewell_parser.add_argument('--farewell_message', default='Goodbye', help='The farewell message')
    farewell_parser.add_argument('--target', default='Joe', help='The person to bid farewell to')


    args = parser.parse_args()

    if args.command == 'greet':
        greet(args.greeting , args.target)
    elif args.command == 'farewell':
        farewell(args.farewell_message, args.target)
"""
O/P:
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ ./say_it.py farewell --farewell_message Goodbye --target bob
Goodbye bob
"""
