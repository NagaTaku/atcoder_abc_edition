import copy

n = int(input())
t = list(map(int,input().split()))
m = int(input())


for i in range(m):
    x,y = map(int,input().split())
    s = copy.copy(t)
    s[x-1] = y
    ans = 0

    for j in range(n):
        ans += s[j]

    print(ans)