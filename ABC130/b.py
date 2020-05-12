n, x = map(int, input().split())

L = list(map(int, input().split()))

dis = 0
ans = 1
for i in range(n+1):
    dis += L[i]
    if dis > x:
        dis -= L[i]
        break
    ans += 1

print(ans)
