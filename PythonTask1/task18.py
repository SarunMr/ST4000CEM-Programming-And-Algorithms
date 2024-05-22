'''A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased. The program should read three integers: the number of students in each of the three 
classes, a, b and c respectively.'''

a_students = int(input("Enter number of students in class a"))
b_students = int(input("Enter number of students in class b"))
c_students = int(input("Enter number of students in class c"))

total_students = a_students + b_students + c_students
total_purchase_bench = total_students // 2

print(f"For the total number of students {total_students} \nThe school should purchase {total_purchase_bench} amount of benches")
