number=int(input())
count=0
L=[]
for i in range(1,number+1):
    if((number%i)==0):
        L.append(i)
for j in L:
    if((j%2)!=0):
        print(j,end=" ")
