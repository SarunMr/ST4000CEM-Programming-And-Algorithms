'''Write a program to accept percentage and display the category according to the following criteria:
    Percentage                                      Category
    <40                                              Failed
    >=40 and <55                                      Fair
    >=55 and <65                                      Good
    >=65                                            Excellent   '''

percentage = float(input("What Percentage did you score? "))

if percentage < 40:
    print("Failed")
elif  40 <= percentage <55:
    print("Fair") 
elif 55 <= percentage <65:
    print("Good")
elif 65 <= percentage <= 100:
    print("Excellent")
else:
    print("Error Percentage!!")    