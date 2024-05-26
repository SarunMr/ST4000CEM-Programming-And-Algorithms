#write a program to display integer from of a list. given list=[1,"a","c",2,3,4]

List=[1,"a","c",2,3,4]

for i in  range(len(List)):
    a = str(List[i])
    if a.isdigit():
        print(List[i])

