n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        if l[i]==l[j]:
            continue
        for k in range(j+1, n):
            if l[i]==l[k] or l[j]==l[k]:
                continue
            if l[j]+l[i] > l[k]:
                ans += 1
print(ans)