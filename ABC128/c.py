
n, m = map(int, input().split())

need = [None] * m
ans = 0

for i in range(m):
    s = list(map(int, input().split()))
    need[i] = s

p = list(map(int, input().split()))

for i in range(2 ** n):
    zentou = 1
    status = [0] * n

    for j in range(n):
        if ((i >> j) & 1):
            status[j] = 1

    for j in range(m):
        total = 0
        for t in range(1, len(need[j])):
            if status[need[j][t]-1] == 1:
                total += 1
        
        if total%2 != p[j]:
            zentou = 0

    if zentou == 1:
        ans += 1

print(ans)