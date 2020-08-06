n = int(input())
a = list(map(int, input().split()))
ans = [None]*n
for i in range(n):
    ans[a[i]-1] = i+1
print(' '.join(map(str,ans)))