'''Accept the age, gender('M', 'F'), number of days and display the wages accordingly.
Age                       Gender          Wage/day
>=18 and <30                 M                700
                             F               750
>=30 and <=40                M               800
                             F               850   '''

age = int(input("Enter Age? "))
gender = input("Enter Gender(M,F)? ").capitalize()
number_days = int(input("Enter Days? "))

GENDER_Junior = { "M":700 *number_days , "F":750*number_days }
GENDER_Senior = { "M":800 *number_days , "F":850*number_days }

if 18 <= age < 30:
    if gender in GENDER_Junior:
        print(f"Your wage is Rs{GENDER_Junior[gender]} in {number_days} Days.") 
    else:
        print("Not a gender")
elif 30 <= age <= 40:
    if gender in GENDER_Senior:
        print(f"Your wage is Rs{GENDER_Senior[gender]} in {number_days} Days.") 
    else:
        print("Not a gender")
else:
    print("Invaild Age")