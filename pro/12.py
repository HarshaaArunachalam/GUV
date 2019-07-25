u,v=map(int,input().split())
w=list(map(int,input().split()))
n=[]
for u in range(v):
    j,k=map(int,input().split())
    y=sum(w[j-1:k])
    n.append(y)
for j in n:
    print(j)
