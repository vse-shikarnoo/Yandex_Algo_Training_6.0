n,k=input().split()
l=[int(x) for x in input().split()]
prSum=[]
prSum.append(0)
for i in range(1,int(n)+1):
    prSum.append(prSum[i-1]+l[i-1])

res = 0
r = 0

for i in range(len(prSum)):
    while r<len(prSum) and prSum[r]-prSum[i]<int(k):
        r+=1
    if r==len(prSum):
        break
    if prSum[r]-prSum[i]==int(k):
        res+=1

print(res)