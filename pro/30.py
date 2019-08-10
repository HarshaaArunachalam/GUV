a=input(" ")
b=0
for i in range(0,len(a)):
    c=a[0:i]+a[i+1::]
    if int(c)%8==0:
        b=1
        break
if b==1:
    print("yes")
else:
    print("no")
