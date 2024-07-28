#!/usr/bin/env python
"""
import click

@click.command()
@click.option('--greeting', default='Hiya', help = 'How do you want to greet?')
@click.option('--name', default='Tammy',help='Who do you want to greet?')
def greet(greeting,name):
    print(f"{greeting} {name}")

if __name__ == '__main__':
    greet()
"""
"""
O/P: (.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload$ ./Using_Click.py --greeti
ng Hola --name Gaurav
Hola Gaurav
"""

"""
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload$ ./Using_Click.py --help
Usage: Using_Click.py [OPTIONS]

Options:
  --greeting TEXT  How do you want to greet?
  --name TEXT      Who do you want to greet?
  --help           Show this message and exit.
"""

#Nested Command with 'Click'

#You can create more complex CLI applications with nested command using 'click.group'.
# This allows you to organize related commands together.

import click

@click.group()
def cli():
    pass

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', default='World',help='The person to greet.')

def hello(count,name):
    for _ in range(count):
        click.echo(f'Hello {name}!')

@click.command()
@click.option('--name', default='World',help='The person to say goodbye to. ')
def goodbye(name):
    click.echo(f'Goodbye {name}!')

cli.add_command(hello)
cli.add_command(goodbye)

if __name__ == '__main__':
    cli()
"""
O/P:(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload$ ./Using_Click.py hello --
count 3 --name Gaurav
Hello Gaurav!
Hello Gaurav!
Hello Gaurav!
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload$ ./Using_Click.py goodbye --name Gaurav
Goodbye Gaurav!
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload$ 
"""