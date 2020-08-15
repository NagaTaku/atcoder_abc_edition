import math
fact = [None]*1000001

x, y = map(int, input().split())
total = x+y
ans = 0
MOD = 10**9+7

fact[1] = 1
for i in range(2,1000001):
    fact[i] = fact[i-1]*i

print('fin')
if total%3 == 0 and max(x,y) <= min(x,y)*2:
    step = int(total/3)
    sa = abs(x-y)
    a = int((step-sa)/2)
    b = int((step+sa)/2)
    ans = fact[step] / (fact[a]*fact[b])

ans %= MOD
print(int(ans))