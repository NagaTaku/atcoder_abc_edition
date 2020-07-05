n, k = map(int, input().split())
a = list(map(int, input().split()))
wari = (10**9)+7
ans = 1

a = sorted(a, reverse=True)

if a[0] < 0 and k%2 == 1:
    for i in range(k):
        ans *= a.pop(0)
else:
    tobashi = False
    for i in range(k):
        if tobashi:
            tobashi = False
            continue

        if abs(a[0]) >= abs(a[-1]):
            ans *= a.pop(0)
        else:
            if a[-1]*a[-2] > a[0]*a[1]:
                if i < k-1:
                    ans *= (a.pop())
                    ans *= (a.pop())
                    tobashi = True
                else:
                    ans *= a.pop(0)

ans = ans%wari
print(ans)