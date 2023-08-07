# Loop works in range

#For Loop: For is a iteration based loop
#Iteration: Repetitive execution of the same block of code over and over is reffered as iteration

for i in range(10):
    print(i)
print("\n")

# range(start,end,increment/decrement)
#here end is end - 1

import time
for a in range(5,11):
    print(a)
print("\n")

for z in range(2,21,2):
    print(z)
print("\n")

#While loop: While is a condition based loop
#While loop is used to repeat specific block of code unknown no. of times, until condition 
#is met

i = 0
while i < 5:
    print(i)
    i = i + 1
# Output will be zero and it will run till infinite time until we stop it
     
while True:
    time.sleep(2) 
    print("boom")    















