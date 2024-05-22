# Write a program to accept two numbers and mathematical operators and perform operation accordingly.

a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
sign = input("Enter operator(+,-,*,/):")

OPERATOR = { "+":a+b , "-":a-b , "*":a*b , "/":a/b }

if sign in OPERATOR:
    print(OPERATOR[sign])

else:
    print("Invalid Operator")
    