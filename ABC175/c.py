x, k, d = map(int, input().split())
ans = 0

if x < 0:
    x = (-1)*x
if k*d <= x:
    ans = x-k*d
else:
    sho = x//d
    now = x-d*sho
    k -= sho
    if d-now < now:
        k -= 1
        now = d-now
    if k%2 == 0:
        ans = now
    else:
        ans = d-now
print(ans)