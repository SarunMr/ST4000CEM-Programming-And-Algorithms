#Python program to calculate the sum of all the even numbers within the given range.

n = int(input("Enter a number? "))
sum = 0 

for i in range(0,n+1,2):
    sum += i
    
print(f'sum of even numbers till {n} is {sum}')