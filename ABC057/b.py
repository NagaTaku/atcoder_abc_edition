n, m = map(int, input().split())

a = []
b = []
c = []
d = []
for i in range(n):
    ax, by = map(int, input().split())
    a.append(ax)
    b.append(by)
for i in range(m):
    cx, dy = map(int, input().split())
    c.append(cx)
    d.append(dy)

for i in range(n):
    min_dis = float('inf')
    ans = 0
    for j in range(m):
        if min_dis > abs(a[i]-c[j])+abs(b[i]-d[j]):
            min_dis = abs(a[i]-c[j])+abs(b[i]-d[j])
            ans = j+1
    print(ans)

