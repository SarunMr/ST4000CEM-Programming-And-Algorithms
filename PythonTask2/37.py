# Python program to count the number of even and odd numbers from a series of numbers.
n = int(input("Enter a range? "))

odd = 0
even = 0

for i in range(1,n+1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Number of odd is {odd}")
print(f"Number of even is {even}")