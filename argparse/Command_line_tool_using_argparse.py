
#Using Argparse

# Using Argparse in python simplifies the creation and management of command line interface
# It allows you to define commands and flags along with their help messages, making it 
# easier to parse arguments.

#Step by Step guide to Using 'argparse'

# 1. Creating an ArgumentParser Object
# The first step is to create an 'ArgumentParser' object with a description of your
# program

import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Maritime control')

# 2. Add Arguments
# You can add positional arguments and optional flags using the 'add_argument' method.
# Positional arguments do not begin with a dash, while optional flags do.

parser.add_argument('message',help='Message to echo')
parser.add_argument('--twice', '-t', help='Do it twice', action='store_true')

# 3. Parse Arguments
# Use the 'parse_args' method to parse the command-line arguments. This method returns an
# object with attributes corresponding to the arguments.

args = parser.parse_args()

# 4 Access Parsed Arguments
# You can access the parsed arguments using the attributes of the returned object.
print(args.message)
if args.twice:
    print(args.message)

#Automatically Generated Help and Usage Message
#'argparse' generates help and usage message based on the provided description and help
# texts
"""
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ ./simple_parse.py hello
hello

(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ ./simple_parse.py --help
usage: simple_parse.py [-h] [--twice] message

Maritime control

positional arguments:
  message      Message to echo

options:
  -h, --help   show this help message and exit
  --twice, -t  Do it twice
"""

#Advanced Usage: Subcommands
# Many command-line tools use nested commands for organization, such as 'git stash pop'.
#With 'argparse', you can create subparser for subcommands.

#Example of how to implement a maritime application with subcommands for ships and sailors

#!/usr/bin/env python
"""
Maritime Control Application
"""
import argparse

if __name__ == '__main__':
    parser = argparse.Argument.Parser(description='Maritime control')
    subparsers = parser.add_subparsers(dest='command')

    # Ship Command
    ship_parser = subparsers.add_parser('ship', help='Commands related to ships')
    ship_parser.add_argument('name', help='Name of the ship')
    ship_parser.add_argument('--sail','-s',help='Sail the ship', action='store_true')

    # Ship command

    sailor_parser = subparsers.add_parser('sailor',help='Commands related to sailors')
    sailor_parser.add_argument('name',help='Name of the sailor')
    sailor_parser.add_argument('--assign','-a',help='Assign the sailor to a ship',metavar='SHIP')

    args = parser.parse_args()

    if args.command == 'ship':
        print(f'Ship name: {args.name}')
        if args.sail:
            print(f'Sailing the ship {args.name}')
    
    elif args.command == 'sailor':
        print(f'Sailor name: {args.name}')
        if args.assign:
            print(f'Assigning {args.name} to ship {args.assign}')

"""
O/P: (.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ ./simple_parse.py ship Titanic --sail
Ship name: Titanic
Sailing the ship Titanic
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ ./simple_parse.py sailor John --assign Titanic
Sailor name: John
Assigning John to ship Titanic
"""