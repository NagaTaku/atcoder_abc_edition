n, m = map(int, input().split())
ex = [0 for i in range(n)]
fri = {}

for i in range(m):
    a, b = map(int, input().split())
    if ex[a-1] == 0 and ex[b-1] == 0:
        if a > b:
            a, b = b, a
        ex[a-1] = a
        ex[b-1] = a
        fri[a] = [a, b]
    elif ex[a-1] == 0:
        ex[a-1] = ex[b-1]
        fri[ex[b-1]].append(a)
    elif ex[b-1] == 0:
        ex[b-1] = ex[a-1]
        fri[ex[a-1]].append(b)
    elif ex[a-1] == ex[b-1]:
        continue
    else:
        shozoku = min(ex[a-1], ex[b-1])
        mu = max(ex[a-1], ex[b-1])
        for j in range(len(fri[mu])):
            ex[fri[mu][j]-1] = shozoku
        fri[shozoku].extend(fri.pop(mu))

ans = 1
for key in fri:
    ans = max(ans, len(fri[key]))
print(ans)