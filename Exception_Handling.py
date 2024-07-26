#Exception Handling: prevent program crashes
#Use try-except to handle unexpected error
#You can have multiple except blocks to handle different types of execution

import builtins
cloud_envs = ["aws","azure","gcp"]
try:
    print(cloud_envs[4])
    raise Exception("This is a new exception") #We can create our own exception through raise
                                               #exception
except:
    print("exception handled")
finally: #Content in finally always executed regardless of exception
    print("I will excecute anyway")

print("This code should run")


try:
    #print(cloud_envs[200])
    a = 10
    b = 0
    c = a/b

except ZeroDivisionError as e:
    print("1", e)
except IndexError as e:
    print("2", e)

print(dir(builtins))
