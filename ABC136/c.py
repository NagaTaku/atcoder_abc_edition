N = int(input())
h = list(map(int, input().split()))
ans = True
MIN = h[0]-1

for i in range(N-1):
    MIN = max(MIN, h[i]-1)
    if h[i] > h[i+1]:
        if h[i]-h[i+1] > 1:
            ans = False
            break
        else:
            if MIN > h[i+1]:
                ans = False
                break

if ans:
    print('Yes')
else:
    print('No')