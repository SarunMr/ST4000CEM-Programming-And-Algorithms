#Given list is [1,2,3,4] but expected output is [1,"a",2,4]

lst = [2,1,3,4]
newlst = []

for i in range(len(lst)):
    if lst[i] == 3:
        continue
    newlst.append(lst[i])
    if lst[i] == 1:
        newlst.append("a")
    

print(newlst)

