
#Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". Hint a=["ram","shyam",1,2] expected output:  Hello!ram Hello!shyam

a = ["ram","shyam",1,2]

for i in a:
    if isinstance(i,str):
        print(f"hello!,{i}",end = " ")