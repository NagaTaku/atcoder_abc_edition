def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

a, b, c = map(int, input().split())

if c%gcd(a, b) == 0:
    print('YES')
else:
    print('NO') 