#Given list is [1,2,3,4,5] separate the elements into odd and even categories.

lst = [1,2,3,4,5]
oddlst = []
evenlst = []

for i in range(len(lst)):
    if lst[i] % 2 == 0:
        evenlst.append(lst[i])
    else:
        oddlst.append(lst[i])

print(f"Your list containing even numbers {evenlst}")
print(F"Your list containing odd numbers {oddlst}")