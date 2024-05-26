# Python program to check the validity of username and password input by users


for i in range(5):
    name = input("Enter name? ")
    password = input("Enter password? ") 

    if len(name) >= 10 and len(password) >= 10 and  "*" in password:
        print(f"Your name {name}")
        print(f"Your password {password}")
        break    
    else:
         print("Your name must contain at least 10 characters.")
         print("Your password must contain '*' and contain minimum length 10 and ")

    if i == 3:
        print("This is your last attempt to to fullfill requirement or your you will be blocked.")

