s = input()

n = len(s)
ans = 0


#bit演算を利用して、全探索
#＋の入る箇所はn-1なのでそれを利用
#ひとまず＋を入れるか入れないか調査し、１つずつ入れていき出来上がった文字列を＋で分割して合計する
for i in range(2**(n-1)):
    f = s[0]
    for j in range(n-1):
        if ((i >> j) & 1):
            f += "+"
        f += s[j+1]
    
    ans += sum(map(int, f.split("+")))

print(ans)