x,y=input().split()
x=int(x)
y=int(y)
s=[]
for i in range(1,100000):
    if((i%x==0) and i%y==0):
        s.append(i)
        a=s[0]
print(a)
