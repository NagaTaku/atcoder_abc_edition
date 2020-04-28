s = input()

f = s[0]
ans = 0

for i in range(1,len(s)):
    if s[i] != f:
        ans += 1
        f = s[i]

print(ans)
