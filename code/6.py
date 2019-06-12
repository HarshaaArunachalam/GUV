string1,string2=input().split()
string1=set(string1)
string2=set(string2)
if len(string1)==len(string2):
    print("yes")
else:
    print("no")
