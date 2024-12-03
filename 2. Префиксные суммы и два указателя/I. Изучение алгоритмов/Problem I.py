from typing import List, Dict

class Algo:
    def __init__(self, num=-1, a=-1, b=-1):
        self.number = num
        self.a = a
        self.b = b


n = int(input())
inpA = list(map(int, input().split()))
inpB = list(map(int, input().split()))
inp = list(map(int, input().split()))

vec = [Algo(i + 1, inpA[i], inpB[i]) for i in range(n)]

sortedA = sorted(vec, key=lambda x: (-x.a, -x.b, x.number))
sortedB = sorted(vec, key=lambda x: (-x.b, -x.a, x.number))

mp: Dict[int, bool] = {}
pa = 0
pb = 0
ans = []

for i in range(n):
    if inp[i] == 0 and pa < n:
        if not mp.get(sortedA[pa].number, False):
            ans.append(sortedA[pa].number)
            mp[sortedA[pa].number] = True
            pa += 1
        else:
            while pa < n:
                if not mp.get(sortedA[pa].number, False):
                    ans.append(sortedA[pa].number)
                    mp[sortedA[pa].number] = True
                    pa += 1
                    break
                pa += 1
    elif inp[i] == 1 and pb < n:
        if not mp.get(sortedB[pb].number, False):
            ans.append(sortedB[pb].number)
            mp[sortedB[pb].number] = True
            pb += 1
        else:
            while pb < n:
                if not mp.get(sortedB[pb].number, False):
                    ans.append(sortedB[pb].number)
                    mp[sortedB[pb].number] = True
                    pb += 1
                    break
                pb += 1
    else:
        break

print(" ".join(map(str, ans)))