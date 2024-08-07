#File Handling

#Entire process of handling a file using python is called file handling.
absolute_path = r'/home/gauravmtwt1/Documents/Python for DevOps/Class8_function_and_filehandling/file_handling/myfile.txt'

#Read operation

file_obj = open(absolute_path,"r") #function call
#print(file_obj.read()) #process
#print(type(file_obj.read()))
print(file_obj.readlines())
print(file_obj.readline(10)) #When we use readline, it will iterate the index
file_obj.close() #close

#readlines is more preferred than readline.

#Write Operation
#Write mode first clear old content then write new content.
file_obj = open(absolute_path,"w")
file_obj.write("I am writing in myfile.txt using file handling in file_handler") #write
file_obj.close()


#Append Mode
absolute_path = r'/home/gauravmtwt1/Documents/Python for DevOps/Class8_function_and_filehandling/file_handling/myfile.txt'

file_obj = open(absolute_path,"a") #append
file_obj.write(" Mayra mera pyaara baccha") #append add new content to exist content
file_obj.close


# Creating a new text file
absolute_path1 = r'/home/gauravmtwt1/Documents/Python for DevOps/Class8_function_and_filehandling/file_handling/mynew_file2.txt'
try:
    
    f = open(absolute_path1, 'r')
except FileNotFoundError:
    print("error handled")
    f = open(absolute_path1, 'w+')
    f.write("Mayra smart baby hain papa ka")
finally:
    f.close()   
    print("This code should run")



