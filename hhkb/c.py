n = int(input())
p = list(map(int, input().split()))
buf = [0] * 200001

idx = 0
for i in range(n):
    buf[p[i]] = 1
    while buf[idx] == 1:
        idx += 1
    print(idx)