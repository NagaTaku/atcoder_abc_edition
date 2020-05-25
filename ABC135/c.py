N = int(input())
Monster = list(map(int, input().split()))
Yusha = list(map(int, input().split()))

total = 0

for i in range(N+1):
    if i > 0:
        Min = min(Monster[i], Yusha[i-1])
        Monster[i] -= Min
        Yusha[i-1] -= Min
        total += Min

    if i < N:
        Min = min(Monster[i], Yusha[i])
        Monster[i] -= Min
        Yusha[i] -= Min
        total += Min

print(total)