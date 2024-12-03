n = int(input())
c = 1000000007
l = [int(x) for x in input().split()]

pref = [l[0]]
for i in range(1, n):
    pref.append((l[i] + pref[i - 1]))

#print(pref)

pref2 = [pref[0]*l[1]]
for i in range(1, n-2):
    pref2.append((pref[i]*l[i+1]+pref2[i-1])%c)

#print(pref2)

res=0
i=1

while i<n-1:
    res+=(pref2[-i]*l[-i])%c
    i+=1
print(res%c)