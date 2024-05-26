a = input("Enter string? ")

add = 0

for i in a:
    if i.isspace():
        add += 1

print("Number of space :{}".format(add))