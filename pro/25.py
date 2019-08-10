def lis(arr,size):
    r=[]
    count=1
    for i in range(0,size-1):
        if arr[i]<arr[i+1]:
            count+=1
        else:
            r.append(count)
            count=1
    r.append(count)
    print(max(r))
size=int(input())
arr=list(map(int,input(" ").split(" ")))
lis(arr,size)
