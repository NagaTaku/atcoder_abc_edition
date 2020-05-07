n, k = map(int, input().split())

if n >= k:
    kati = (n -(k-1))/n
else:
    kati = 0

for i in range(1, min(n+1, k)):
    total = i
    kakuritsu = 1/n
    while total < k:
        kakuritsu *= 0.5
        total *= 2
    kati += kakuritsu

print(kati)

