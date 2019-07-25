u=int(input())
v=list(map(int,input().split()))
w=0
for i in range(0,u):
    for j in range(0,i):
        if v[j]<v[i]:
            w=w+v[j]
print(w)
