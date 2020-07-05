import math

n = int(input())
a = list(map(int, input().split()))
ans = 0

a = sorted(a, reverse=True)
for i in range(1,n):
    x = math.floor(i/2)
    ans += a[x]

print(ans)