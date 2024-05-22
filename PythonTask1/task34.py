# i,j,k=3,5,7    OUTPUT: 5,5,7
# i,j,k=2,-5,9   OUTPUT: 9,-5,9
# i,j,k=8,15,12  OUTPUT: 15,15,12
# i,j,k=13,15,13 OUTPUT: 13,13,13
# i,j,k=3,5,17   OUTPUT: 5,5,17
i,j,k=25,15,17
'''OUTPUT 17,15,17'''


if i<j:
    if j<k:
        i = j
    else:
        j = k
else:
    if j>k:
        j = i
    else:
        i = k 

print(i,j,k)


