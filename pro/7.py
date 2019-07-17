xyz=int(input())
sum=0
for i in range(0,xyz):
    if(pow(2,i)>xyz):
        break
    sum=xyz-pow(2,i)
print(sum)
