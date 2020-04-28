def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

n = int(input())

divisors = make_divisors(n)

l = len(divisors)
#print(divisors)

ans = float('inf')
for i in range(l):
    a = divisors[i]
    b = int(n/a)
    m = max([a,b])
    keta = 1
    while m > 9:
        m = int(m/10)
        keta += 1
    ans = min([ans, keta])

print(ans)
