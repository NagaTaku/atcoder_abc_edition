n, k = map(int, input().split())

A = []

for i in range(n):
    c = []
    a, b = map(int, input().split())
    c.append(a)
    c.append(b)
    A.append(c)

A.sort(key=lambda x:x[0])


f = k
i = 0
while f > 0:
    f -= A[i][1]
    i += 1

print(A[i-1][0])
