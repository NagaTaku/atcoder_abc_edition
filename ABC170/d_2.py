# ネット参照
# 数列の最大値＋１のサイズの配列を作り、初期値１を入れる
# 数列の小さい順に要素を見て、その値のdpが1の時はその値より小さい数列の倍数になっていない（その値を割り切れる数列の値がなかった）ことなので、答えに追加し、最大値までのその値の倍数のdpを全て0にする
# これを繰り返すことで、他の要素で割り切れる時は0が、割り切れない時は1が入っているため、下から数えて1が入っている個数を数え上げる。

n = int(input())
a = list(map(int, input().split()))
a.sort()
aMax = a[-1]
ans = 0
dp = [1] * (aMax+1)

for i in range(n-1):
    p = a[i]
    if dp[p] == 1:
        for j in range(aMax//p+1):
            dp[p*j] = 0
        if a[i] != a[i+1]:
            ans += 1
if dp[aMax] == 1:
    ans += 1
print(ans)