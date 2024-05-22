#A company decided to give bonus of 5% to employee if his/her year of service is more than 5years. Ask user for their salary and year of service and print the net bonus amount.

salary = float(input("What is your salary? "))
expirence = int(input("Enter your service in year? "))

if expirence > 5:
    print(f"You will recive '5%' bonus and your net bonus amount is {0.05 * salary}")
else:
    print("Sorry you did not recive any bonus")