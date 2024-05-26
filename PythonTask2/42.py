# python program to check a number is perfect number

num = int(input("Enter number? "))
perfect_num = 0

for i in range(1,num):
    if num % i == 0:
        perfect_num += i

if perfect_num == num:
    print(f"{num} is perfect number.")
else:
    print(f"{num} is not perfect number.")

