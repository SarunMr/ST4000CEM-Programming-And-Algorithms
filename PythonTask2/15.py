#Python program that accepts a string and calculate the number of digits and letters and space.

a  = input("Enter random string? ")

alpha = 0
digit = 0
space = 0

for i in a:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        alpha += 1
    else:
        space +=1

print("Number of Characters:",alpha)
print("Number of Digit",digit)
print("Number of Space",space)
