n, m = map(int, input().split())
MOD = 10**9+7

a = [True]*(n+1)

for i in range(m):
    s = int(input())
    a[s] = False

dp = [0]*(n+1)

dp[0] = 1
if a[1]:
    dp[1] = 1

for i in range(2,n+1):
    if a[i-1]:
        dp[i] += dp[i-1]
    if a[i-2]:
        dp[i] += dp[i-2]
    dp[i] %= MOD

print(dp[n])




"""
def factorial(x, mod=10**9+7):
    # x!
    # 階乗
    # ex) factorial(5) = 120
    tmp = 1
    for i in range(1, x+1):
        tmp = (tmp * i)
    return tmp



def step(t):
    total = 0
    buf2 = int(t/2)

    for i in range(buf2+1):
        buf1 = t-(i*2)
        buf12 = buf1 + i
        buf_ue = factorial(buf12)
        buf_sita1 = factorial(buf1)
        buf_sita2 = factorial(i)
        total += int(buf_ue / (buf_sita1*buf_sita2))

    return total


n, m = map(int, input().split())
MOD = 10**9+7
total = 1
now = 0

for i in range(m):
    a = int(input())
    if a == now:
        total = 0
        break
    elif a == now+1:
        now = a+1
    else:
        print(a-1-now)
        total *= step(a-1-now)
        now = a+1

total *= step(n-now)
total = total%MOD
print(total)
"""