'''
 Accept the following from the user and calculate the percentage of class attended:
a. Total number of working days
b. Total number of days for absent
After calculating percentage show that, if the percentage is less than 75, than student will not be able to sit in exam.    '''

number_of_workingDays = int(input("Present Days? "))
number_of_absent = int(input("Absent Days? "))

total_Days = number_of_workingDays - number_of_absent
percentage = (total_Days / number_of_workingDays) * 100

if percentage < 75:
    print(f"Your attndance percentage is {percentage}")
    print(" You will not be able to sit in exam.")
else:
    print(f"Your attndance percentage is {percentage}")
    print("You can sit in exam.")