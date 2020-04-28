s = input()

g = 0;p = 0
total = 0

for i in range(len(s)):
    if s[i] == 'g':
        if p < g:
            p += 1
            total += 1
        else:
            g += 1
    elif s[i] == 'p':
        if p < g:
            p += 1
        else:
            g += 1
            total -= 1

print(total)
    