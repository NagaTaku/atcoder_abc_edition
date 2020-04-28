a, b, x = map(int, input().split())

p = 0
y = int(b//x) + 1

i = 1
while x*i <= b:
    if a <= x*i:
        p = x*i
        break
    i += 1

if p != 0:
    t = b-p
    s = t//x
    ans = s + 1
    if a == 0:
        ans += 1
    print(ans)
elif a == 0:
    print(1)
else:
    print(0)