num=int(input())
start=input()
for i in range(num-1):
    end=input()
    length=len(end)
    if len(start)<len(end):
        length=len(start)
    for j in range(length):
        if(start[j] != end[j]):
            start=start[:j]
            break
print(start)


