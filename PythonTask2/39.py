# given number is prime or not

n = int(input("Enter range? "))
count = 0
for  i in range(1,n+1):   
    if n % i == 0:
        count += 1
    
if count == 2:
    print("isprime")
else:
    print("not prime")
  