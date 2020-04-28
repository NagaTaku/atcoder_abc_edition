n = int(input())
a = list(map(int, input().split()))

f = 1

if n%2 == 0:
    ans = [2]*(n//2)
    #print(ans)
    for i in range(n):
        if a[i]%2 == 0:
            f = 0
            break
        x = a[i]//2
        ans[x] -= 1

else:
    ans = [2]*((n+1)//2)
    ans[0] -= 1
    for i in range(n):
        if a[i]%2 != 0:
            f = 0
            break
        x = a[i]//2
        ans[x] -= 1

for i in range(len(ans)):
    if ans[i] != 0:
        f = 0
        break

if f == 0:
    print(f)
else:
    print((2**(n//2))%1000000007)




"""
if n%2 == 0:
    for i in range(n//2):
        if a.count(i*2+1) != 2:
            f = 0
            break

else:
    if a.count(0) != 1:
        f = 0
    for i in range(n//2):
        if a.count((i+1)*2) != 2:
            f = 0
            break

if f == 0:
    print(f)
else:
    print(2**(n//2))
"""