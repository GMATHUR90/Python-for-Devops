
#Set does not support duplicates
#Set does follow orders and arrange numbers in ascending order
#set_of_num = {None}
#print(type(set_of_num))

#set_of_num2 = {}
#print(type(set_of_num2))

set_1 = {1,1,1,1,1,2,2,2,2,3,3,4,45,4,34,3,2}
set_2 = {1,1,1,1,45,6,6,7,7,8,4,3,3}
print(set_1.intersection(set_2)) #finding common numbers in set_1 and set_2
print(set_1.union(set_2)) # Merging set_1 and set_2 output

list_of_env = ["dev","stg","prd","tst","qa","qa","dev"]
list_of_env = list(set(list_of_env))
print(list_of_env)

#Functionalities of sets:
# Add
# Remove
# Union
# Intersection
# Difference
# Subset / Superset

set_1 = {}
print(type(set_1))

set_of_cars = {"audi", "bmw", "volvo","audi"}
another_set_of_car = {"bmw","Mahindra","Maruti","Tata"}
#print(set_of_cars)
#print(another_set_of_car)

#Add an element
#set_of_cars.add("skoda")
#print(set_of_cars)

# Remove an element
#set_of_cars.remove("bmw")
#print(set_of_cars) 

#Union
#set_3 = set_of_cars.union(another_set_of_car)
#print(set_3)

#Intersection
#intersection_set_4 = set_of_cars.intersection(another_set_of_car)
#print(intersection_set_4)

#Difference:
#A - B = Only A
difference_set_5 = set_of_cars.difference(another_set_of_car)
print(difference_set_5)

a = {1,2,3,4,5}
b = {2,5,6,7,8}

print(b.difference(a)) 

# subset and superset

c = {1,5,6,7,8,9} #superset
d = {1,5,6}       #subset

print(d.issubset(c))
print(c.issuperset(d))