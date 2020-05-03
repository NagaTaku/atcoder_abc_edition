n, k = map(int, input().split())

ha = [0] * n
for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))

    for j in range(d):
        buf = a[j]-1
        ha[buf] += 1

ans = 0
for i in range(n):
    if ha[i] == 0:
        ans += 1

print(ans)


