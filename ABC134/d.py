N = int(input())
a = list(map(int, input().split()))

last_ans = 0

for i in range(2 ** N):
    hako = [0]*N
    for j in range(N):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            hako[j] = 1

    #print(hako)
    ans = 0
    for kijun in range(1,N+1):
        baisuu = 1
        total = 0
        while kijun*baisuu <= N:
            if hako[kijun*baisuu-1] == 1:
                total += 1
            baisuu += 1

        total %= 2
        if a[kijun-1] != total:
            ans = 1
            break

    if ans == 0:
        last_ans = 1
        break

if last_ans == 1:
    print(hako.count(1))
    if hako.count(1) != 0:
        buf = [i+1 for i, x in enumerate(hako) if x == 1]
        print(' '.join(map(str, buf)))
else:
    print(-1)