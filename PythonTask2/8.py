#given list is [1,2,3,4] but expected output in new list [2,3,4,5]

List = [1,2,3,4]
newlist = []

for i in range(len(List)):
    if List[i] == 1:
        continue
    newlist.append(List[i])

newlist.append(5)

print(newlist)