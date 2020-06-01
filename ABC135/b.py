N = int(input())
p = list(map(int, input().split()))

p2 = sorted(p)

cnt = 0
for i in range(N):
    if p[i] != p2[i]:
        cnt += 1
    if cnt == 3:
        break

if cnt == 3:
    print('NO')
else:
    print('YES')
