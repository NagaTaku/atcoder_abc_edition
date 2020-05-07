n, m = map(int, input().split())


l_max = 0
r_min = float('inf')

for i in range(m):
    l, r = map(int, input().split())
    l_max = max(l_max, l)
    r_min = min(r_min, r)

if r_min >= l_max:
    ans = int(r_min-l_max+1)
else :
    ans = 0
print(ans)

"""
L = [None] * m
R = [None] * m

for i in range(m):
    L[i], R[i] = map(int, input().split())

can = [1]*n

for i in range(m):
    p = set()
    for j in range(m+1):
        t = i+j
        if t < m:
            p.add(L[t])
        else:
            p.add(R[t-m])

    for i in range(n):
        if can[i] == 1:
            if not i+1 in p:
                can[i] = 0

print(can.count(1))
"""