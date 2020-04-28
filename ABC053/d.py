# コピぺ
# かぶっている値が奇数の場合は余分に１つ多く消してしまうので、被りがない値の個数−1
# かぶっている値が偶数の場合は被りがない値がそのまま答えとなる

N = int(input())
A = list(map(int, input().split()))
setA = set(A)
if len(setA) % 2 != 0:
    print(len(setA))
else:
    print(len(setA) - 1)