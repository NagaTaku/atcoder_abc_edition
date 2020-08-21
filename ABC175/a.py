s = list(input())
ans = 0

for i in range(3):
    if s[i]=='R':
        if ans==0:
            ans = 1
        else:
            if s[i-1]=='R':
                ans+=1
print(ans)