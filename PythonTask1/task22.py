# Write a program to check whether a person is eligible for voting or not. (accept age from user).

age = int(input("Enter age? "))

if age > 18:
    print("You can vote!!")
else:
    print("You are underage to vote!!!")
