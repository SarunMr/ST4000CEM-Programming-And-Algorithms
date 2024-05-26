#Write a python program to display all the prime numbers within a given range.

n = int(input("Enter range? "))


for i in range(2,n+1):
    prime = True
    
    for j in range(2,int(i ** 0.5)+1):
        print(j)
        if i % j == 0:
             prime = False
             break
    if prime:
       print(i,end = " ")



            





            

        
  