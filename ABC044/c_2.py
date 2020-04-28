#できない！！！！2020/01

import numpy as np
hi = np.zeros((5000, 60), np.int64)
hi[0,0] = 1

n, a = map(int, input().split())

#入力で得られた文字列を分割して配列にいれる
x = list(map(int, input().split()))

for i in x:
    hi_ = hi.copy()








"""""""""""""""""""""""""""
def kaiki(j, k, s, l):
    sum = 0
    if j == 0 & k == 0 & s == 0:
        sum += 1
    elif j >= 1:
        if s < l[j-1]:
            sum += kaiki(j-1, k, s, l)
        elif k >= 1 & s >= x[j-1]:
            sum += kaiki(j-1, k, s, l) + kaiki(j-1, k-1, s-x[j-1], l)        
    else:
        sum += 0
    return sum

n, a = map(int, input().split())

#入力で得られた文字列を分割して配列にいれる
x = list(map(int, input().split()))

res = 0
for p in range(1,n):
    res += kaiki(n, p, p*a, x)

print(res)

"""""""""""""""""""""""""""""""""
