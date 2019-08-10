a=int(input(" "))
b=list(map(int,input().split()))
b.sort()
c=0
d=0
for i in range(len(b)):
    if b[i]>=c:
        d=d+1
    c=c+b[i]
print(d)
