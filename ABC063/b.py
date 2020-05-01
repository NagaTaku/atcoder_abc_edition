s = input()

buf1 = set()

for i in range(len(s)):
    buf1.add(s[i])

if len(s) == len(buf1):
    print('yes')
else:
    print('no')