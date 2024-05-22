'''Accept the number of days from the user and calculate the charge for library according to following:
    Till five days: Rs 2/day
    Six to ten days: Rs 3/day
    11 to 15 days: Rs 4/day
    After 15 days: Rs 5/day     '''

number_days = int(input("How many days did you lend book? "))

if number_days <= 5:
    print(f"You will be charged Rs{2 * number_days}")
elif 5 < number_days < 11:
    print(f"You will be charged Rs{3 * number_days}")
elif  10 < number_days < 15:
    print(f"You will be charged Rs{4 * number_days}")
else:
    print(f"You will be charged Rs{5 * number_days}")