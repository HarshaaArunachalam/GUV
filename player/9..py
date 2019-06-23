N,K=input().split()
N=int(N)
K=int(K)
lis=[]
for i in range(N,K):
    if(i>1):
        for i in range(2,i):
            if(i%2==0):
                break
        else:
            lis.append(i)
print(len(lis))
