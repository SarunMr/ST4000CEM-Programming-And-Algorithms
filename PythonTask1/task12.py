'''A company decided to give bonus to employee according to following criteria:
    Time period of service       Bonus
    More than 10 years            10%
    >=6 and <=10                   8%
    Less than 6 years              5%     '''

expirence = int(input("Give your service years? "))

if expirence > 10:
    print("You will recive '10%' bonus")
elif 6 <= expirence <= 10:
    print("You will recive '8%' bonus")
else:
    print("You will recive '5%' bonus")