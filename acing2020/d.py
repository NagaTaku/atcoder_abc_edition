import copy

def popcount(n):
    bin_str = bin(n)[2:]
    l = list(bin_str)
    ans = l.count('1')
    return ans


def f(n):
    ans = 0
    while n != 0:
        n = n % popcount(n)
        ans += 1
        #print(n)
    return ans

n = int(input())
x = list(input())

for i in range(n):
    buf = copy.copy(x)
    if buf[i] == '1':
        buf[i] = '0'
    else:
        buf[i] = '1'
    #num_one = buf.count('1')
    num = int('0b' + ''.join(buf), 2)
    print(f(num))
