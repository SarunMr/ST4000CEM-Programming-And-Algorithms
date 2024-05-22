# Write a python program which accepts the radius of circle from user and compute the area.

radius = float(input("Enter radius:"))
if radius > 0:
    print(f"Area of circle is {3.14 * radius * radius}")
else:
    ("Enter positive number.")