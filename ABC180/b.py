import math

n = int(input())
x = list(map(abs, map(int, input().split())))
man = 0
yu = 0
che = 0

for i in range(n):
    man += x[i]
    yu += x[i]**2

che = max(x)
yu = math.sqrt(yu)

print(man)
print(yu)
print(che)