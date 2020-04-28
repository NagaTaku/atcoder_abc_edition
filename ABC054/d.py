#途中棄権
import numpy as np
n, ma, mb = map(int, input().split())

a = [0]*n
b = [0]*n
c = [0]*n
min_cost = 1000000000

for i in range(n):
    a[i], b[i], c[i] = map(int, input().split())

for i in range(2**n):
    total_a = 0
    total_b = 0
    total_cost = 0
    for j in range(n):
        if((i >> j) & 1):
            total_a += a[j]
            total_b += b[j]
            total_cost += c[j]
    if (total_cost != 0 and total_a/total_b == ma/mb):
        min_cost = min(min_cost,total_cost)
    
if (min_cost < 1000000000):
    print(min_cost)
else:
    print('-1')
