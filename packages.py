import os # import is a key word to bring library here
import shutil

#print(os.getcwd()) # To print current working directory

#print(os.uname())

print(shutil.disk_usage("/")) # / means root in linux ; shutil is used to use shell script 
                            # in python and size in Bytes

#floor division(//):it roundoff the division output to nearby wholeno, less than what originally
# it is
total, used, free = shutil.disk_usage("/")
print(f"Total disk space is: {total // (2**30)} GB") ##Fstring(Formatted String)
print("used space is: ", used // (2**30))
print("free space is: ", free // (2**30))

 
