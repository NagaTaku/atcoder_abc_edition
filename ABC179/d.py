n, k = map(int, input().split())
s = []
MOD = 998244353

for i in range(k):
    l, r = map(int, input().split())
    for j in range(r-l+1):
        s.append(l+j)

print(s)
num = len(s)

for i in range(2 ** num):

    for j in range(num):
        if ((i >> j) & 1):
            