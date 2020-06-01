N = int(input())
A = list(map(int, input().split()))

tree = 0
ans = 0
can = True
for i in range(N, -1, -1):
    Max = 2**i
    tree += A[i]
    if tree > Max:
        can = False
        break
    elif tree > Max/2:
        ans += tree
        tree = int(Max/2)

    elif tree >= 0:
        ans += tree
    print(tree, ans)

if can:
    print(ans)
else:
    print(-1)
    