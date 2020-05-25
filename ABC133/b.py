import math

N, D = map(int, input().split())
X = [None]*N

for i in range(N):
    buf = list(map(int, input().split()))
    X[i] = buf

ans = 0

for i in range(N-1):
    for j in range(i+1, N):
        buf = 0
        for p in range(D):
            buf += (X[i][p]-X[j][p])*(X[i][p]-X[j][p])
        buf1 = math.sqrt(buf)
        if buf1 == int(buf1):
            ans += 1
print(ans)