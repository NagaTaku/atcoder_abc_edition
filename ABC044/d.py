#できないです2020/2/2

def floor(a):
    return int(a)


def f(b, n):
    if n < b:
        return n
    else:
        p = int(n/b)
        return (f(b, p) + n%b)
    pass


m = int(input())
s = int(input())

#ans = f(m, s)
#print(ans)

for i in range(1,11):
    t = f(i, m)
    print(t)

