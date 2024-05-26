#Python program to calculate the sum of all the odd numbers within the given range.

n = int(input("Enter a number? "))
sum = 0 

for i in range(1,n+1,2):
    sum += i
    
print(f'sum of odd numbers till {n} is {sum}')
