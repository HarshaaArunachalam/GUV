a=int(input(" "))
b=0
c=0
d=[]
while b<90 and b<a:
    e=0
    for j in str(a-b):
        e+=int(j)
    if e+(a-b)==a:
        c+=1
        d.append(a-b)
    b+=1
print(c)
for b in d:
    print(b)
