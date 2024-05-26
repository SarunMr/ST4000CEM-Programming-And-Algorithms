#Given list is lst=[1,2,3,4] but print 1 2 and 4 only

lst=[1,2,3,4]

for i in range(len(lst)):
    if lst[i] == 3:
        continue
    print(lst[i])
