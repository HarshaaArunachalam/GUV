num=int(input())
count=0
for i in range(num):
    for j in range(i+1,num):
        count=count+1
print(count)
