#Given list is [1,2,3,"d",4,5,"a"] separate the elements based on their data types

lst = [1,2,3,"d",4,5,"a"]
intlst = []
strlst = []

for i in range(len(lst)):
    if isinstance(lst[i],str):
        strlst.append(lst[i])
    else:
        intlst.append(lst[i])

print(f"Your list containing string numbers {strlst}")
print(F"Your list containing integers numbers {intlst}")