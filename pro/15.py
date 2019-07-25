x=int(input())
y=list(map(int,input().split()))
z=[]
for i in range(x):
    y.sort(reverse=True)
print(*y,sep="\n")
