N, T = map(int, input().split())

t = list(map(int, input().split()))

x = N*T

for i in range(1,N):
    sa = t[i] - t[i-1]
    if sa < T:
        x -= (T-sa)

print(x)
