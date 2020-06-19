x, y = map(int, input().split())
ans = True

if x*4 < y or x*2 > y or y%2 == 1 :
    ans = False

if ans:
    print('Yes')
else:
    print('No')
