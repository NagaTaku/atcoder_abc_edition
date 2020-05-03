a, b, n = map(int, input().split())

M = 0
for x in range(n+1):
    M = max(int(a*x/b)-(a*int(x/b)), M)

print(M)