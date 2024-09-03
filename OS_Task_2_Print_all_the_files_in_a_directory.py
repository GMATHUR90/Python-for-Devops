import os
# Input File Path
input_file_path = r'/home/gauravmtwt1/Documents/Python for DevOps'
# Output File Path
output_file_path = r'/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops/OS_Task_2_Output.txt'
# Check if input file path is a file
if os.path.exists(input_file_path):
    if os.path.isfile(input_file_path):
        print(f"{input_file_path} exists as a file")
    else:
        # If the path is directory, print the directory name
        print(f"{input_file_path} exists as a directory")
        # Open the output file in write mode
        with open(output_file_path, 'w') as file_output:
            # Iterate through each file/directory in the input file path
            for file in os.listdir(input_file_path):
                print(file)
                # Write the output in the output file
                file_output.write(file + "\n")
    
else:
    # If the input path does not exist, print a message
    print("Input file Path does not exists")




       