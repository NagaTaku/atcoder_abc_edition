n, m = map(int, input().split())

if abs(n-m)>1:
    ans = 0
else:
    if m < n:
        n, m = m, n

    total_n = 1
    for i in range(1,n+1):
        total_n *= i
        if total_n >= 1000000007:
            total_n = total_n % 1000000007

    if n != m:
        ans = (total_n * total_n * m) % 1000000007
    else:
        ans = (total_n * total_n * 2) % 1000000007

print(int(ans))
