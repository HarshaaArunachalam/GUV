N,K=input().split()
N=int(N)
K=int(K)
lists=[]
for i in range(1,K+1):
    if(N%i==0 and K%i==0):
        lists.append(i)
print(max(lists))
