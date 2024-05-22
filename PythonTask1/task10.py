# Accept the age of 4 people and display the oldest one.

age = int(input("Enter age 1:"))
age1 = int(input("Enter age 2:"))
age2 = int(input("Enter age 3:"))
age3 = int(input("Enter age 4:"))

if age > age1 and age > age2 and age3:
    print(f"This age {age} is older.")
elif age1 > age2 and age1 > age3:
    print(f"This age {age1} is older.")
elif age1 > age3:
    print(f"This age {age2} is older.")
else:
    print(f"This age {age3} is older.")