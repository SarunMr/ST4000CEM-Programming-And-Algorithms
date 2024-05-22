# Write a program to check whether a number entered is three digit number or not.

number = int(input("Enter any number:"))

if len(str(number)) < 3:
    print(f"Your number {number} is three digit")
else:
    print(f"Your number {number} is not three digit")