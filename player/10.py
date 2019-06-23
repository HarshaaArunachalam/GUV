N,K=input().split()
sum=0
if(len(N)==len(K)):
    for i in range(0,len(N)):
        if(N[i]!=K[i]):
            sum=sum+1
if(sum==1):
    print("yes")
else:
    print("no")
