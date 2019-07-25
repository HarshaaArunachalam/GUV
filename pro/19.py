a=int(input())
b=[]
c=[]
for i in range(0,a):
    b.append(input().split())
for j in b:
    for k in j:
        c.append(int(k))
for r in sorted(c):
    print(r,end=" ")
