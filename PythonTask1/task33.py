'''
Accept input from user

if given number is a multiple of both 3 and 5 prints "FizzBuzz" instead of number

if  given number is a multiple of 3 but not 5 prints "Fizz" instead of number

if given number is a multiple of 5 but not 3 prints "Buzz" instead of number

if given number is not multiple of 3 or 5 prints value as usual. 
'''

number = int(input("Enter Any number? "))

if number % 3 == 0:
    if number % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
elif number % 5 == 0:
    print("Buzz")        
else:
    print(number)