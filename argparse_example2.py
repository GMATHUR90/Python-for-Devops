#!/usr/bin/env python

#Command line tool using argparse

import argparse

def sail():
    ship_name = 'Your Ship'
    print(f"{ship_name} is setting sail")

def list_ships():
    ships = ['John B', 'Yankee Clipper', 'Pequod']
    print(f"Ships: {' , '.join(ships)}")

def greet(greeting,name):
    message = f'{greeting} {name}'
    print(message)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Maritime control')
    parser.add_argument('--twice', '-t', help='Do it twice', action='store_true')

    subparsers = parser.add_subparsers(dest='func')

    ship_parser =  subparsers.add_parser('ships', help = 'Ship related commands')
    ship_parser.add_argument('command', choices=['list','sail'])

    sailor_parser = subparsers.add_parser('sailors', help='Talk to a sailor')
    sailor_parser.add_argument('name', help= 'Sailor name')
    sailor_parser.add_argument('--greeting', '-g', help='Greeting', default='Ahoy there')

    args = parser.parse_args()

    if args.func == 'sailors':
        greet(args.greeting, args.name)
    elif args.func == 'ships':
        if args.command == 'list':
            list_ships()
        else:
            sail()


"""
O/P: (.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ chmod +x argparse_example2.py 
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ ls -la argparse_example2.py 
-rwxrwxr-x 1 gauravmtwt1 gauravmtwt1 1185 Jul 25 07:15 argparse_example2.py
"""

"""
O/P: (.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ ./argparse_example2.py ships list
Ships: John B , Yankee Clipper , Pequod
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ ./argparse_example2.py ships sail
Your Ship is setting sail
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ ./argparse_example2.py sailors John
Ahoy there John
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ ./argparse_example2.py sailors John --greeting "Hello"
Hello John
"""