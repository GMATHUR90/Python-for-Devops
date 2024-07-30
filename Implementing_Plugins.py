#!/usr/bin/env python
#Various Command-Line Tool Libraries:

#1.argparse:
# Pros: Detailed control, good for complex interfaces.
# Use Case: When you need to separate UI code from business logic.

#2. click:
# Pros: Balances ease and control, less verbose than argparse
# Use Case: Suitable for most use cases

#3. fire:
# Pros: Minimal, quick to expose objects, ideals for debugging and getting acquainted
#       with new code.
# Use Case: When you need to access code quickly without an existing command-line
#           interface.

#Implementing Plug-ins:

# Definition: Plug-ins are user-supplied code extensions that add functionality to your
#             application.

# Applications: Widely used in both large applications(like Autodesk's Maya) and minimal
#               framework(like Flask).

# Example of a Simple Plugin System:

#!/usr/bin/env python

import fire
import pkgutil
import importlib

def find_and_run_plugins(plugin_prefix):
    plugins = {}
    # Discover and Load Plugins
    print(f"Discovering plugins with prefix: {plugin_prefix}")
    for _, name, _ in pkgutil.iter_modules():
        if name.startswith(plugin_prefix):
            module = importlib.import_module(name)
            plugins[name] = module
    
    # Run Plugins
    for name, module in plugins.items():
        print(f"Running plugin {name}")
        module.run()

if __name__ == '__main__':
    fire.Fire()

"""
O/P: (.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload$ ./Implementing_Plugins.py find_and_run_plugins foo_plugin
Discovering plugins with prefix: foo_plugin
Running plugin foo_plugin_a
Running plugin A
Running plugin foo_plugin_b
Running plugin A
"""