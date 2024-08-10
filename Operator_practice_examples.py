# 1. Arithmetic Operator

# Addition

a = 5
b = 3

result_1 = a+b
print("The addition of a and b is :", result_1)

# Subtraction

result_2 = a-b
print("The subtraction of a and b is:", result_2)

# Multiplication

result_3 = a * b
print("The multiplication of a and b is : ", result_3)

# Division 
result_4 = a/b
print("The division of a and b is: ", result_4)

# Floor Division
result_5 = a//b
print("The floor division of a and b is: ", result_5)

# Modulus(%)
result_6=a%b
print("The modulus of a and b is:  ", result_6)

# Exponentiation(**)
result_7 = a**b
print("The exponentiation of a and b is: ", result_7)

# 2. Assignment Operator(+)

result_8 = a 
print("The value of a assigned to result_8: ", result_8)

# i. Addition Assignment(+=)
result_9 = 7
result_9 += a
print("The addition assignment on result_9 is: ",result_9)

# ii. Subtraction Assignment(-=)
result_10 = 7
result_10 -= a
print("The subtraction assignment on result_10 is: ", result_10)

# iii. Multiplication Assignment(*=)
result_11 = 7
result_11 *=a
print("The multiplication assignment on result_11 is: ", result_11)

# iv. Division Assignment(/=):
result_12 = 7
result_12 /= a
print("The division assignment on result_12 is: ", result_12)

# v. Modulus Assignment(%=):
result_13 = 7
result_13 %= a
print("The modulus assignment on result_13 is: ", result_13)

# vi Exponentiation Assignment(*=):
result_14 =7
result_14 *= a
print("The exponentiation on result_14 is: ", result_14)

# 3. Logical Operator

x = True
y = False
z = True

# i. AND(and) Operator

result_15 = x and y
print("The and operator for x and y: ", result_15)

result_15_a = x and z
print("The and operator for x and z: ", result_15_a)

# ii. OR(or) Operator
result_16 = x or y
print("The or operator for x and y: ", result_16)

# iii. NOT(not) Operator
result_17 = x != y
print("The not operator for x and y is: ", result_17)

result_17_a = x!= z
print("The not operator for x and z is: ", result_17_a)

# 4. Membership Operator
#sequence or collection : list , tuple , string
# in : Return true if left operand is present in sequence on the right
# not in: Return True if left operand is not present in sequence on the right

fruits = ["apple","banana","cherry"]
car = ("maruti", "alto")

result_18 = "apple" in fruits
print("Does apple available in fruit list: ",result_18)

result_18_a = "mango" in fruits
print("Does mango available in fruit list: ", result_18_a)

result_18_b =  "Pinapple" not in fruits
print("Does Pinapple not in fruits list: ", result_18_b)

# 5. Relational Operational
d = 5
e = 5
f = 9
# 1. Equal to(==):

result_19 = d == e

print("If d is equal to e: ", result_19)

# 2. Not equal to(!=):

result_20 = d != f
print("If d is not equal to e: ", result_20)

# 3. Greater than(>):

result_21 = d > f
print("If d is greater than f: ", result_21)

# 4. Less than(<):

result_22 = d < f
print("If d is less than f: ", result_22)

# 5. Greater than or equal to (>=):

result_23 = d >= f
print("If d is greater than or equal to: ", result_23)

# 6. Less than or equal to (<=):
result_24 = d <= f
print("If d is less than or equal to: ", result_24)
