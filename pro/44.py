N,P,Q,R=input().split()
lists=list(map(int,input().split()))
N=int(N)
P=int(P)
Q=int(Q)
R=int(R)

c=[]
for i in range(0,len(lists)):
    for j in range(i,len(lists)):
        for k in range(j,len(lists)):
            c.append(P*lists[i]+Q*lists[j]+R*lists[k])
print(max(c))
