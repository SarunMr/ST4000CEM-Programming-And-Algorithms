# Accept the grades from the user and display the grade according to the following criteria.

marks = int(input("Enter your marks."))

if 25 > marks:
    print("D")
elif 25 <= marks < 45:
    print("C")
elif 45 <= marks < 50:
    print("B")
elif 50 <= marks < 60:
    print("B+")
elif 60 <= marks <= 80:
    print("A")
elif 80 < marks <= 100:
    print("A+")
else:
    print("Invalid Marks")