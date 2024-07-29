#!/usr/bin/env python

#Command line tool using tool

#cli: Top Level Group: Act as main entry point for cli
#ships: Subgroups: Contain commands related to ships
#Command under 'ships':
#      1. 'sail': Print a message indicating a ship is setting sail
#      2. 'list_ships': Print a list of predefined ship names
#'sailors': Talks to a sailor with customizable greeting

import click

@click.group()
def cli():
    pass

@click.group(help='Ship related commands')
def ships():
    pass

cli.add_command(ships)

@ships.command(help='Sail a ship')
def sail():
    ship_name = 'Your ship'
    print(f"{ship_name} is getting sail")

@ships.command(help='List all the ships')
def list_ships():
    ships = ['John B', 'Yankee Clipper', 'Pequod']
    print(f"Ships: {', '.join(ships)}")

@cli.command(help='Talk to a sailor')
@click.option('--greeting',default='Ahoy there', help='Greeting for sailor')
@click.argument('name')
def sailors(greeting, name):
    message = f'{greeting} {name}'
    print(message)

if __name__ == '__main__':
    cli()

"""
.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload$ chmod +x Using_Click_Example_2.py 
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload$ ls -la Using_Click_Example_2.py 
-rwxrwxr-x 1 gauravmtwt1 gauravmtwt1 723 Jul 29 06:59 Using_Click_Example_2.py

(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload$ ./Using_Click_Example_2.py --help
Usage: Using_Click_Example_2.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  sailors  Talk to a sailor
  ships    Ship related commands

(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload$ ./Using_Click_Example_2.py ships list-ships
Ships: John B, Yankee Clipper, Pequod

(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload$ ./Using_Click_Example_2.py ships sail
Your ship is getting sail
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload$ ./Using_Click_Example_2.py sailors --greeting "Hello" ROger
Hello ROger
"""