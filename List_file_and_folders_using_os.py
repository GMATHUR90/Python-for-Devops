import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None , "Permission denied"
    
def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()

    for folder_path in folder_paths:
        files , error_message = list_files_in_folder(folder_path)
        if files:
            print(f"Files in {folder_path}: ")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()

"""
O/P:: (.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents$ /home/gauravmtwt1/Documents/git-demo/.venv/bin/python "/home/gauravmtwt1/Documents/Python for DevOps/github_python_topic_upload/List_file_and_folders_using_os.py"
Enter a list of folder paths separated by spaces: /opt
Files in /opt: 
containerd
az
pt
google
microsoft
"""
