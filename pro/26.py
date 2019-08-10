a=int(input(" "))
s=list(map(int,input().split()))
b=[]
c=1
for i in s:
    if i not in b:
        b.append(i)
for i in range(0,len(b)-1):
    if b[i]<b[i+1]:
        x+=1
print(x)
