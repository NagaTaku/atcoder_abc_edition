s = list(input())
t = list(input())
sa = float('inf')

for i in range(len(s)-len(t)+1):
    s_part = s[i:(i+len(t))]
    huitti = len(t)
    for j in range(len(t)):
        if s_part[j] == t[j]:
            huitti -= 1
    sa = min(sa, huitti)

print(sa)