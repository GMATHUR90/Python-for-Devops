#Accepting Command-Line Arguments

#To make your script accept command-line arguments, you can use the 'sys.argv' list.

#!/usr/bin/env python

import sys

if __name__ == '__main__':
    print(f"The first argument: '{sys.argv[0]}'")
    print(f"The second argument: '{sys.argv[1]}'")
    print(f"The third argument: '{sys.argv[2]}'")
    print(f"The fourth argument: '{sys.argv[3]}'")

#chmod +x ./sys_argv.py
"""
O/P: (.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ ./sys_argv.py --a-flag some-value 13
The first argument: './sys_argv.py'
The second argument: '--a-flag'
The third argument: 'some-value'
The fourth argument: '13'
"""    

#Parsing Command-Line Arguments:

#For more complex argument parsing, consider using the "argparse" module, which is a part
# of the Python standard library.
#sys module provide access to some variables used or maintained by the interpreter
# and to functions that interact strongly with the interpreter.

"""
#!/usr/bin/env python

import sys

def say_it(greeting,target):
    message = f'{greeting} {target}'
    print(message)

#This line ensures that the following code block runs only if the script is executed
# directly(not improted as module)    
if __name__ == '__main__':
    greeting = 'Hello'
    target = 'Joe'
# if '--help' is present in the command-line arguments,The script pring 
# the usage message and exits.
    if '--help' in sys.argv:
        help_message = f"Usage: {sys.argv[0]} --name <NAME> --greeting <GREETING>"
        print(help_message)
        sys.exit()
#if '--name' is present in the command-line-arguments, the script find the index of
'--name', adds 1 to get the index of the name value, and updates the 'target' variable.
# It checks if the index is bounds to avoid an IndexError
    if '--name' in sys.argv:
        name_index = sys.argv.index('--name') + 1
        if name_index < len(sys.argv):
            target = sys.argv[name_index]

# Similar to the '--name' flag this block checks for '--greeting', finds its index,and
# updates the 'greeting' varibale with the provided value.            

    if '--greeting' in sys.argv:
        greeting_index = sys.argv.index('--greeting') + 1
        if greeting_index < len(sys.argv):
            greeting = sys.argv[greeting_index]

    say_it(greeting,target)
"""
"""
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps$ ./sys_argv.py --name Gaurav --greeting Suprabhat
Suprabhat Gaurav

"""