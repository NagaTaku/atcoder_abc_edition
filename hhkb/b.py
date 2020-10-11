h, w = map(int, input().split())
a = []
ans = 0
for i in range(h):
    a.append(input())

for i in range(w):
    for j in range(h):
        if a[j][i] == '.':
            if i != w-1:
                if a[j][i+1] == '.':
                    ans += 1
            if j != h-1:
                if a[j+1][i] == '.':
                    ans += 1

print(ans)