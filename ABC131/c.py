import math
#import fractions

def lcm(a, b):
    return (a * b) // math.gcd(a, b) 
    #return (a * b) // fractions.gcd(a, b) 


A, B, C, D = map(int, input().split())

#間の数の個数
num = B - A + 1

CD = lcm(C, D)

c = int(num/C)
if num%C != 0 and (num%C > A%C or num%C > (C-(A%C))):
    c += 1

d = int(num/D)
if num%D != 0 and (num%D > A%D or num%D > (D-(A%D))):
    d += 1

cd = int(num/CD)
if num%CD != 0 and (num%CD > A%CD or num%CD > (CD-(A%CD))):
    cd += 1

ans = num - (c + d - cd)
print(ans)