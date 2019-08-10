u,v=map(int,input(" ").split(" "))
temp=[]
x=0
for i in range(u):
    temp.append(list(map(int,input().split())))
for i in range(u):
    for j in range(v-1):
        for k in range(j+1,v+1):
            if temp[i][j:k]==[1]*len(temp[i][j:k]):
                if all(temp[l+i][j:k]==[1]*len(temp[l+i][j:k]) for l in range(len(temp[i][j:k])-1)):
                    if len(temp[i][j:k])>x:
                        x=len(temp[i][j:k])
if len(temp)==1 and len(temp[0])==1 and temp[0][0]==1:
    print(1)
for i in range(x):
    print(*[1]*x)
