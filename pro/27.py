a,b=map(int,input(" ").split(" "))
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=[]
f=0
for i in range(a):
    x=d[i]/c[i]
    e.append(x)
while b>=0 and len(e)>0:
    mind=e.index(max(e))
    if b>=c[mind]:
        f=f+d[mind]
        b=b-d[mind]
    c.pop(mind)
    d.pop(mind)
    e.pop(mind)
print(f)
