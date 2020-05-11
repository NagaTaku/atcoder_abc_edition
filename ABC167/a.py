s = input()
t = input()

ans = 0

if len(s)+1 == len(t):
    if s == t[:-1]:
        ans = 1

if ans == 1:
    print('Yes')
else:
    print('No')