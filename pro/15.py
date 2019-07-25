u=int(input())
v=list(map(int,input().split()))
w=[]
for i in range(u):
    v.sort(reverse=True)
print(*v,sep="\n")
