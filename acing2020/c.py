import math
from itertools import combinations_with_replacement

def calc(t):
    return t[0]*t[0] + t[1]*t[1] + t[2]*t[2] + t[0]*t[1] + t[1]*t[2] + t[2]*t[0]


n = int(input())
ans = [0]*n
n_root = math.floor(math.sqrt(n))+1

for pattern in combinations_with_replacement(range(1, n_root + 1), 3):
    pattern = list(pattern)
    buf = calc(pattern)
    print(pattern)
    if buf <= n:
        if pattern[0] == pattern[1] == pattern[2]:
            ans[buf-1] += 1
        elif pattern[0] == pattern[1] or pattern[1] == pattern[2] or pattern[0] == pattern[2]:
            ans[buf-1] += 3
        else:
            ans[buf-1] += 6

#[print(a) for a in ans]
print(ans)