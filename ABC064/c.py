n = int(input())

a = list(map(int, input().split()))


ans = [0] * 8
hi_rate = 0

for i in range(n):
    buf = int(a[i]/400)
    if buf <= 7:
        ans[buf] += 1
    else:
        hi_rate += 1

low_rate = 0
for i in range(8):
    if ans[i] > 0:
        low_rate += 1

if low_rate == 0:
    minm = 1
    maxm = hi_rate
else:
    minm = low_rate
    maxm = low_rate + hi_rate

print(str(minm) + ' ' + str(maxm))