import math
n = int(input())
ans = 0

for a in range(1, n):
    buf = math.floor((n-1)/a)
    ans += buf

print(ans)