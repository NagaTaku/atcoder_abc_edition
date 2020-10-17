import math

x, y, a, b = map(int, input().split())
ans = 0

while x*a - x < b:
    x = x*a
    ans += 1
    if x >= y:
        print(ans-1)
        exit()

if b+x < y:
    numB = (y-x)//b
    x += numB * b 
    if x == y and numB > 0:
        numB -= 1
    ans += numB

print(ans)