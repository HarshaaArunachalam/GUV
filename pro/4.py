x,y=map(str,input(" ").split(" "))
z=0
if len(x)>len(y):
    x,y=y,x
u=0
while u<len(x):
    z+=(ord(y[u])-ord(x[u]))
    u+=1
for u in range(u,len(y)):
    z+=ord(y[u])-ord('a')+1
print(z)
