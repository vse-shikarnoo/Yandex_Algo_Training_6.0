n=int(input())
l = [int(x) for x in input().split()]

pref=[0]
prefs=[0]
for i in range(1,n):
    pref.append(l[i-1]+pref[i-1])
    prefs.append(prefs[i-1]+l[i-1]+pref[i-1])
    
#print(pref)
#print(prefs)
    
pref2=[0]
prefe=[0]
for i in range(n-1,0,-1):
    pref2.append(l[i]+pref2[n-i-1])
    prefe.append(prefe[n-i-1]+l[i]+pref2[n-i-1])

#print(pref2)
#print(prefe)

res=prefs[0]+prefe[-1]

for i in range(1,n):
    if prefs[i]+prefe[n-i-1]<res:
        res=prefs[i]+prefe[n-i-1]
        
print(res)