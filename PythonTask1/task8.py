#Write a program to accept the cost price of a bike qnd display the road tax to be paid according to the following criteria:

bike = float(input("Enter your bike cost"))

if bike > 100000:
    road_tax = 0.15 * bike
    print(f"Your bike amount before tax {bike}")
    print(f"Your bike amount after 15% TAX {road_tax}")
elif bike > 50000 and bike <= 100000:
    road_tax = 0.10 * bike
    print(f"Your bike amount before tax {bike}")
    print(f"Your bike amount after 15% TAX {road_tax}")
elif bike <=50000:
    road_tax = 0.05 * bike
    print(f"Your bike amount before tax {bike}")
    print(f"Your bike amount after 15% TAX {road_tax}")
