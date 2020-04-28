n, m = map(int, input().split())

a = []
b = []
sa = n-m
ans = 0

for i in range(n):
    a.append(input())

for i in range(m):
    b.append(input())

for i in range(sa+1):
    for j in range(sa+1):
        for p in range(m):
            if a[i+p][j:j+m] != b[p]:
                break
            if p == m-1:
                ans = 1
        if ans == 1:
            break
    if ans == 1:
        break
if ans == 1:
    print('Yes')
else :
    print('No')
