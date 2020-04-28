n = int(input())

a = list(map(int, input().split()))

total = a[0]
ans = 0
hugo = 0
if total == 0:
    if a[1] >= 0:
        total = -1
        ans = 1
        hugo = -1
    else:
        total = 1
        ans = 1
        hugo = 1
elif total > 0:
    ans = 0
    hugo = 1
elif total < 0:
    ans = 0
    hugo = -1


for i in range(1,n):
    total += a[i]
    if hugo == -1 and total <= 0:
        ans = ans + (1-total)
        total = 1
        hugo = 1
    elif hugo == -1 and total > 0:
        hugo = 1
    elif hugo == 1 and total >= 0:
        ans = ans + (1+total)
        total = -1
        hugo = -1
    elif hugo == 1 and total < 0:
        hugo = -1

print(ans)