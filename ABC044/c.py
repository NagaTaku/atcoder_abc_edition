"""""""""部分点回答"""""""""
n, a = map(int, input().split())

x = list(map(int, input().split()))

res = 0

#二進数で選択、未選択を01で表して全パターンを繰り返す
for i in range(1,2**n):
    sum = 0
    num = 0
    for j in range(n):
        #右方向にシフトして一番右側を判定。１の時は選んでいる状態
        if ((i >> j) & 1):
            sum += x[j]
            num += 1
    if num != 0:
        ave = sum / num
    if ave == a:
        res += 1
print(res)
