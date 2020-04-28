sx, sy, tx, ty = map(int, input().split())

nowx, nowy = sx, sy

ans = ''

for i in range(ty-sy):
    ans += 'U'
for i in range(tx-sx):
    ans += 'R'
for i in range(ty-sy):
    ans += 'D'
for i in range(tx-sx):
    ans += 'L'
ans += 'L'
for i in range(ty-sy):
    ans += 'U'
ans += 'U'
for i in range(tx-sx):
    ans += 'R'
ans += 'R'
ans += 'D'
ans += 'R'
for i in range(ty-sy):
    ans += 'D'
ans += 'D'
for i in range(tx-sx):
    ans += 'L'
ans += 'L'
ans += 'U'

print(ans)
