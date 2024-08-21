 import array

#Syntax: variable_name = array.array('type',[a,b,c])
arr = array.array('f',[1,2,3]) # f: float type of array and i for integer
                               #and [1,2,3]: Insert element 

print(arr)

arr.append(10) #add element in array 

print(arr)

arr.pop() # remove last element from array using index
print(arr)

arr.pop(0)
print(arr)

print(arr[0])
print(arr[0:2])