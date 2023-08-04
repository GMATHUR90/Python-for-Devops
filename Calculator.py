num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

opr = input("Enter the operator: ")
output = None
if opr == "+":
    output = num_1 + num_2

if opr == "-":
    output = num_1 - num_2

if opr == "*":
    output = num_1 * num_2

if opr == "/":
    output = num_1 / num_2

print("The output is : ", output)

if num_1 < 3:
    print("num_1 is less than 3")
elif num_1 == 3:
    print("num_1 is equal to 3")
else:
    print("num_1 is greater than 3")
