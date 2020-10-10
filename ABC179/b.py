n = int(input())
ren = 0
ans = 'No'

for i in range(n):
    d1, d2 = map(int, input().split())
    if d1==d2:
        ren += 1
        if ren >= 3:
            ans = 'Yes'
    else:
        ren = 0

print(ans)
