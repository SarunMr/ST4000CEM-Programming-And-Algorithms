# Write a program to check whether a number is divisible by 7 or not.

number = int(input("Enter any number? "))

if number % 7 == 0:
    print(f"Number {number} is divisible by 7")
else:
    print("Not divisible by 7")