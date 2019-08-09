x=int(input(" "))
y=list(map(int,input().split()))
z=[1]*x
for i in range(x):
    if i==0:
        if y[i]>y[i+1]:
            z[i]=z[i]+z[i+1]
    elif i>0:
        if y[i]>y[i-1]:
            z[i]=z[i]+z[i-1]
print(sum(z))
