N, L = map(int, input().split())

#最初のりんご
f_ringo = 0
#最後のりんご
l_ringo = 0
#りんごの個数
num = 0

if L >= 0:
    #１つ目のりんごを食べる
    f_ringo = L + 2 - 1
    l_ringo = L + N - 1
    num = N - 1

        
elif L < 0 and N+L > 0:
    #味が0のりんごを食べる
    f_ringo = L + 1 - 1
    l_ringo = L + N - 1
    num = N


elif L < 0 and N+L <= 0:
    #最後のりんごを食べる
    f_ringo = L + 1 - 1
    l_ringo = L + N-1 - 1
    num = N - 1

total = ((f_ringo+l_ringo) * int(num/2))
if num%2 == 1:
    ringocenter = f_ringo + int(num/2)
    total += ringocenter

print(total)