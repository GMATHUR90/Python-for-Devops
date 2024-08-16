def update_server_config(file_path, key, value):
    # Read the existing content of the server configuration file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Update the configuration value for the specified key
    with open(file_path, 'w') as file:
        for line in lines:
            # Check if the line start with the specified key
            if key in line:
                # Update the line with the new value
                file.write(key + "=" + value + "\n")
            else:
                #Keep the existing line as it is
                file.write(line)

# Path to the server configuration file
server_config_file = f'Python for DevOps/github_python_topic_upload/Python-for-Devops/Server.conf'

# Key and new value for updating the server configuration
key_to_update = 'MAX_CONNECTIONS'
new_value = input("Enter the new_value: ") #New maximum connections allowed

# Update the server configuration file
update_server_config(server_config_file, key_to_update,new_value)

"""
O/P: Intitial Value: 500
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents$ /home/gauravmtwt1/Documents/git-demo/.venv/bin/python "/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/Update_server.py"
Enter the new_value: 700
Updated calue of MAX_CONNECTIONS = 700
"""