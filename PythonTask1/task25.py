#Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.

number = int(input("Enter any number? "))

if number % 2 == 0:
    if number % 3 == 0:
        print(f"Your number {number} is both divisible by 2 and 3")
    else:
        print(f"Your number {number} is only divisible by 2")
else:
    print(f"Your number  {number} is not divisible by 2 and 3")