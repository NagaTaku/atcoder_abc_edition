h, w = map(int, input().split())
a = []

for i in range(h):
    a.append(input())

ans = []
topdown = ""

for i in range(w+2):
    topdown = topdown + "#"

for i in range(h):
    a[i] = "#" + a[i] + "#"

ans.append(topdown)
for i in range(h):
    ans.append(a[i])
ans.append(topdown)

for i in range(h+2):
    print(ans[i])
