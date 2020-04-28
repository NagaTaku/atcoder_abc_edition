"""
ヒント見て解答
仕組みを利用して解答
最適な戦法で勝負した場合、最終的に残る文字列の状態がababab or ababaの２つのパターン、つまり二種類の文字で先頭と末尾の文字が異なる偶数の文字列と２つの文字が同一の奇数の文字列である。このことを利用して計算する
"""

s = input()

num = len(s)

if (s[0] == s[num-1] and num%2 == 0) or (s[0] != s[num-1] and num%2 != 0):
    print('First')
else:
    print('Second')