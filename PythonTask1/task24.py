"""Accept any city from the user and display monument of that city.
                  City                                 Monument
                  Delhi                               Red Fort
                  Agra                                Taj Mahal
                  Jaipur                              Jal Mahal   """

CITY_DIC = { "Delhi":"Red Fort" , "Agra":"Taj Mahal" , "Jaipur":"Jal Mahal" }

city = input("Enter city name? ").capitalize()

if city in CITY_DIC:
    print(CITY_DIC[city])
else:
    print("This city isn't available.")