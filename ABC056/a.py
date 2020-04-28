a, b = input().split()

if a == 'H':
    ans = b
elif a == 'D':
    if b == 'H':
        ans = 'D'
    elif b == 'D':
        ans = 'H'

print(ans)