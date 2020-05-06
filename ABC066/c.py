n = int(input())

a = list(map(int, input().split()))
b = [None]*n

half = int(n/2)
for i in range(1,n+1):
    t = i%2
    if t != 0:
        b[half+int(i/2)] = a[i-1]
    else:
        b[half-int(i/2)] = a[i-1]

if n%2 == 1:
    for i in range(1,n+1):
        print(b[-i], end=' ')
else:
    for i in range(n):
        print(b[i], end=' ')
    