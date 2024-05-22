#WAP which accepts marks of four subjects and display total marks, percentage and grade.

English = int(input("Enter your marks in English:"))
Nepali = int(input("Enter your marks in Nepali:"))
Math = int(input("Enter your marks in Math:"))
History = int(input("Enter your marks in History:"))
total_marks = English + Nepali + Math + History
percentage = (total_marks/400)*100

if percentage > 70:
    print(f"Your total marks is {total_marks}")
    print("Grades")
    print(f"English:{English}")
    print(f"Nepali:{Nepali}")
    print(f"Math:{Math}")
    print(f"History:{History}")
    print(f"Percentage:{percentage}")
    print("Distinction")

elif percentage > 60:
    print(f"Your total marks is {total_marks}")
    print("Grades")
    print(f"English:{English}")
    print(f"Nepali:{Nepali}")
    print(f"Math:{Math}")
    print(f"History:{History}")
    print(f"Percentage:{percentage}")
    print("First Division")

elif percentage > 40:
    print(f"Your total marks is {total_marks}")
    print("Grades")
    print(f"English:{English}")
    print(f"Nepali:{Nepali}")
    print(f"Math:{Math}")
    print(f"History:{History}")
    print(f"Percentage:{percentage}")
    print("Pass")
    
else:
    print(f"Your total marks is {total_marks}")
    print("Grades")
    print(f"English:{English}")
    print(f"Nepali:{Nepali}")
    print(f"Math:{Math}")
    print(f"History:{History}")
    print(f"Percentage:{percentage}")
    print("Fail")