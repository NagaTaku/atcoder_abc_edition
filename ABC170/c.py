x, n = map(int, input().split())
p = list(map(int, input().split()))
MIN = float('inf')
ans = 0

if x not in p:
    print(x)
else:
    i = 1
    while True:
        if x-i not in p:
            print(x-i)
            break
        elif x+i not in p:
            print(x+i)
            break
        else:
            i += 1