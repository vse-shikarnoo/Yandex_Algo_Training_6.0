# cook your dish here
import sys
from collections import defaultdict

n = int(input())
artef = list(map(int, input().split()))
    
m, k = map(int, input().split())
need = list(map(int, input().split()))
    
counter = [0] * n
for i in range(1, n):
    counter[i] = counter[i-1] + (1 if artef[i-1] == artef[i] else 0)
    
mp = {}
for i in range(n-1, -1, -1):
    mp[counter[i]] = i + 1

counterBlock = [0] * n
for i in range(1, n):
    counterBlock[i] = counterBlock[i-1] + (1 if artef[i-1] > artef[i] else 0)
    
mpBlock = {}
for i in range(n-1, -1, -1):
    mpBlock[counterBlock[i]] = i + 1

result = []
for i in need:
    local_ans = -1
    block = counterBlock[i-1]
    if block in mpBlock and mpBlock[block] == 1:
        local_ans = max(local_ans, mpBlock[0])
    else:
        local_ans = max(local_ans, mpBlock.get(block, -1))
        
    simple = counter[i-1]
    if simple - k <= 0:
        local_ans = max(local_ans, mp.get(0, -1))
    else:
        local_ans = max(local_ans, mp.get(simple - k, -1))
        
    result.append(local_ans)
    
print(" ".join(map(str, result)))

