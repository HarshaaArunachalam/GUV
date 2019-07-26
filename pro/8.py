def GCD(a,b):
    z=0
    c=min(a,b)
    for k in range(c,1,-1):
        if(a%k==0)and (b%k==0):
            return k
            z=1
    if z!=1:
        return 1
x=input()
y=x.split(" ")
z=[]
w=[]
res=[]
z1=int(y[0])
z2=int(y[1])
z3=input()
u=z3.split(" ")
for i in range(len(u)):
    w.append(int(u[i]))
for j in range(z2):
    f=input()
    g=f.split(" ")
    g1=int(g[0])-1
    g2=int(g[1])-1
    s=GCD(w[g1],w[g2])
    res.append(s)
for l in res:
    print(str(l))
