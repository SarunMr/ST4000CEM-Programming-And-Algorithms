#Write a program to check two strings are anagram or not.

print("PROGRAM TO CHECK ANAGRAM")

a = sorted(input("Enter string? "))
b = sorted(input("Enter another string? "))

#Ternery Operator
print("Your string is anagram") if a == b else print("not anagram")


    

