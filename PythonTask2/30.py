# Write a for loop which appends the square of each number to the new list.
n = int(input("Enter a range? "))
newlst = []

for i in range(1,n+1):
    newlst.append(i ** 2)

print(f"Your list containing square of every number upto {n} is {newlst}")