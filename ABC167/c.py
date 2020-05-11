n, m, x = map(int, input().split())

book = [[None]*(m+1)]*n

for i in range(n):
    c = list(map(int, input().split()))
    book[i] = c
        

min_ans = float('inf')
for i in range(2 ** n):
    ans = 0
    rikai = [0]*m
    cost = 0

    for j in range(n):
        if((i >> j) & 1):
            p = book[j]
            for t in range(1,m+1):
                rikai[t-1] += p[t]
            cost += p[0]

    for j in range(m):
        if rikai[j] < x:
            ans = 1

    if ans == 0:
        min_ans = min(min_ans, cost)

if min_ans != float('inf'):
    print(min_ans)
else:
    print(-1)