import math

N = int(input())
al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

x = N
keta = [0]*100
i = 0
while x > 0:
    if x % 26 == 0:
        keta[i] = 26
    else:
        keta[i] = x % 26
    x -= keta[i]
    x = int(x / 26)
    i += 1

ans = ""
for p in range(i):
    ans = al[keta[p]-1] + ans

print(ans)