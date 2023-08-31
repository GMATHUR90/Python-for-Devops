tuple_of_days = ("mon","tue","wed","thu","fri","sat","sun")
list_of_days = ["mon","tue","wed","thu","fri","sat","sun"]
print(tuple_of_days[1]) 
#tuple_of_days[1] = "Tuesday"
list_of_days[1] = "Tuesday"
print(list_of_days[1])

#Tuple does not allow item assignment which means value of tuple can not be 
# changed once declared.

#List allows item assignment which means values of list can be changed.

#Tuple: () and List: []
# Tuple : immutable(Values can not be changed)
# List :  Mutable(Values can be changed)

#Q.Why Tuples are immutable?
#Ans. When Tuples are created, it is stored in RAM in hash form. Hash cannot be changed.
#     Hash allows to store large data in small form.
print(dir(tuple))
print(tuple.__doc__)