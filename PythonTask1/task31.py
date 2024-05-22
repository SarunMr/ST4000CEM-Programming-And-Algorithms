# Accept three numbers from the user and display the second largest number.

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

my_list = [a,b,c].sort()
print("The second largest number between {},{},{} is {}".format(a,b,c,my_list[1]))