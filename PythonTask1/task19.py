'''N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket? The program reads the numbers N and K. It should print the two answers for the questions above.'''

number_of_students = int(input("Enter number of students."))
number_of_apples = int(input("Enter number of apples."))

if number_of_apples > number_of_students:
    print(f"Each student will get {number_of_apples // number_of_students}apple")
    print(f"Remaining apples in basket is {number_of_apples - number_of_students}")

else:
    print("Insufficient apples for students.")
