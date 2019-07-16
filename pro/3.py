u,v=input().split()
w=abs(len(v)-len(u))
for i in range(len(u)):
    if(len(v)==1 and v[i] in u):
        break
    if(u[i]!=v[i]):
        w=w+1
print(w)
