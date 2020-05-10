a, b, c, k = map(int, input().split())

if k <= a:
    print(k)
elif k <= a+b:
    print(a)
else:
    c_num = k - a - b
    total = a - c_num
    print(total)
