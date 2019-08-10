from itertools import permutations
a,b=map(int,input(" ").split(" "))
c=list(map(int,input().split()))
for i in permutations(c,2):
    if sum(i)==b:
        print("yes")
        break
else:
    print("no")
