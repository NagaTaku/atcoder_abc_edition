n = int(input())
a = list(map(int,input().split()))

cost = []

for i in range(-100,101):
    cc = 0
    for j in range(n):
        cc += (i - a[j])*(i - a[j])
    cost.append(cc)

cost.sort()
print(cost[0])