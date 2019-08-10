a=int(input(" "))
b=2**a
lists=[]
for i in range(0,b):
    l=bin(i)[2:].zfill(a)
    if(len(l)<len(bin(2**a-1)[2:1])):
        lists.append([l.count("1"),l])
    else:
        lists.append([l.count("1"),l])
lists.sort()
for i in range(len(lists)):
    print(lists[i][1])
