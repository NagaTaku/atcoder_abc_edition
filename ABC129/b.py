n = int(input())
w = list(map(int, input().split()))

ans = float('inf')

s1 = 0
s2 = 0

for i in range(n):
    s2 += w[i]

for i in range(n-1):
    s1 += w[i]
    s2 -= w[i]
    sa = abs(s1-s2)
    ans = min(sa, ans)

print(ans)
