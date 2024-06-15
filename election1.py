#no of votes
n=int(input())
#no of parties
arr=list(map(int,input().split()))
dict={}
if n==1:
    print(arr[0])
else:
    for i in arr:
        if i in dict:
            dict[i]+= 1
        else:
            dict[i]=1
a=-1
v=list(dict.items())
print(v)
v.sort(reverse=True, key=lambda x:x[1])
print(v)
if len(v)==1:
    a=v[0][0]
else:
    if v[0][1]==v[1][1]:
        a=-1
    else:
        a=v[0][0]
print(a)