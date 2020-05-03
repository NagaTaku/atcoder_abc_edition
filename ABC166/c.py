n, m = map(int, input().split())

h = list(map(int, input().split()))
check = [1] * n

for i in range(m):
    a, b = map(int, input().split())

    if h[a-1] < h[b-1]:
        remove = a-1
        check[remove] = 0
    elif h[a-1] > h[b-1]:
        remove = b-1
        check[remove] = 0
    else:
        check[a-1] = 0
        check[b-1] = 0

ans = check.count(1)

print(ans)
