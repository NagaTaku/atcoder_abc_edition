s = input()

start,end = 0,0
for i in range(len(s)):
    if s[i] == 'A':
        start = i
        break
for i in range(1,len(s)):
    t = -i
    if s[t] == 'Z':
        end = t+1
        break

ans = len(s) + end - start
print(ans)
