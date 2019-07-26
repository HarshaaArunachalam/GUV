n=int(input())
lists=input().split()
lists=list(lists)
count=0
def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i])
                count=count+1
    return sorted(repeated)
if(count>1): 
    print(*Repeat(lists))
else:
    print("unique")
