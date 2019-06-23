strings=input()
for x in range(0,len(strings)):
    if(x%2==0):
        print(strings[x+1],end="")
    else:
        print(strings[x-1],end="")
