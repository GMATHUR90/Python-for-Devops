

#                 Data structure
#                       |
#         -------------------------------
#         |                              |
#    Primitive                      Non Primitive
#        |                               |
#   ----------------               -----------------------------
#   |   |     |    |               |                           |
#  int float str  bool           Linear                    Non-Linear
#                                  |                           |
#                           ----------------------      --------------
#                           |   |         |       |     |    |      
#                         list  Tuple Dictionary Set  Stack Queue

#List

list_of_normalcar = ["Maruti", "Tata","Mahindra","Honda","Ford"]
list_of_supercar = ["Ferari", "Porche", "Bugati"]

list_of_supercar.append("Toyata")

print(list_of_supercar)

print(list_of_supercar[1])
print(list_of_normalcar[3])

for i in list_of_supercar:
    print("Racing on road of italy on " + i)

#print(dir(list_of_supercar))

#print(list_of_supercar.extend.__doc__)
list_of_normalcar.extend(list_of_supercar)
print(list_of_normalcar)

#list of even number
for i in range(0,20,2):
    print(i)

#list of odd number

for j in range(0,20,3):
    print(j)

"""
"""
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))   
n = int(input("Enter the value of n: "))


final_list = []
for d in range(a+1):
    for e in range(b+1):
        for f in range(c+1):
            #print([d,e,f])
            if d+e+f != n:
                final_list.append([d,e,f])
print(final_list) 


final_list_comp = [[x,y,z] for x in range(a+1) for y in range(b+1) for z in range(c+1) if a+b+c != n]
print(final_list_comp)

list_of_normalcar = ["Maruti", "Tata","Mahindra","Honda","Ford"]
list_of_supercar = ["Ferari", "Porche", "Bugati"]

list_comp_l = [["The normal car " + i + " running on the street along with suparcar " + j + " in italy "] for i in list_of_normalcar for j in list_of_supercar]

print(list_comp_l)
list_of_normalcar.extend(list_of_supercar)
print(list_of_normalcar)

list_1 = [1,3,2,54,6,74,8]
print(list_1.count(54)) # count: how many time that element appears in list
