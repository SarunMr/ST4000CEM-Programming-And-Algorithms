# program to check given number is palindrome or not

a = input("Enter a number")
b = a[::-1]

if a == b:
    print("palindrome")
else:
    print("not palindrome")

