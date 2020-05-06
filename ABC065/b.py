n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

check = [1]*n
p = 1
ans = 1
total = 0
while check[p-1] == 1:
    total += 1
    check[p-1] = 0
    if a[p-1] == 2:
        ans = 0
        break
    
    p = a[p-1]


if ans == 1:
    total = -1
print(total)