u,v=map(int,input().split())
w=list(map(int,input().split()))
n=[]
for u in range(v):
    c=list(map(int,input().split()))
    n.append(c)
for s in n:
    m=0
    for k in range(s[0]-1,s[1]):
        m=m^w[k]
    print(m)
