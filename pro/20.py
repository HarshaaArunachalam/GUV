u,v=map(int,input(" ").split(" "))
lists=list(map(int,input().split()))
lists.sort(reverse=True)
x=0
tot=v
for i in lists:
    if tot>=i:
        r=int(tot/i)
        x+=r
        tot=tot-(i*r)
    if tot==0:
        break
if tot==0:
    print(x)
