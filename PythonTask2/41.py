#program to check given number is armstrong or not

num = int(input("Enter any number?"))
arm = 0 
check = num

while num > 0:
    digit = num % 10
    digit = digit ** 3
    arm += digit
    num = num // 10

if arm == check:
    print("armstrong number")
else:
    print("not armstrong")

