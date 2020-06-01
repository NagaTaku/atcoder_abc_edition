N = int(input())
A = list(map(int, input().split()))

total = 1
if 0 in A:
    N = 0
    total = 0
for i in range(N):
    total *= A[i]
    if total>1000000000000000000:
        total = -1
        break

print(total)