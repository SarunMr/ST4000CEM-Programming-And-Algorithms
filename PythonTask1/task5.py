#Check whether the user input number is even or odd and display it to user.

number = int(input("Enter any number:"))

if number % 2 == 0:
    print(f"Your input {number} is Even")
else:
    print(f"Your input {number} is Odd")