n=input()
l=[int(x) for x in input().split()]
res=[]
res.append(l[0])
for i in range(1,len(l)):
    res.append(res[i-1]+l[i])
print(*res)