string=input()
li=[]
for i in string:
    if i not in li:
       li.append(i)
print(*li,sep="")
