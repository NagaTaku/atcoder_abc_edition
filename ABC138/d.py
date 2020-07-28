import sys
sys.setrecursionlimit(10 ** 6)
import sys
def input():
    return sys.stdin.readline()[:-1]
N , Q = map(int,input().split())
graph = [[] for _ in range(N)]
point = [0] * N
for _ in range(N - 1):
    a , b = map(int,input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
#print(graph)
for _ in range(Q):
    a , b = map(int,input().split())
    a = a - 1
    point[a] += b
# dfsを用いて累積和を計算する
# 初期状態だと前の値がないためデフォルト引数に-1を代入
def dfs(now , prev = -1):
    for next in graph[now]:
        # 次のノードが前に参照した値の時はcontinue
        if next == prev:
            continue
        # 現在の値を次のポイントに加算することで累積和をとる
        point[next] += point[now]
        # 次のノードと現在のノードを引数にdfsを継続する
        dfs(next , now)

dfs(0)
print(*point)
"""
import sys
def input():
    return sys.stdin.readline()[:-1]

n, q = map(int, input().split())
nodes = [[] for _ in range(n+1)]
nodes[1].append(0)
counts = [0 for _ in range(n+1)]

for i in range(n-1):
    pea, chi = map(int, input().split())
    nodes[chi].append(pea)
    nodes[pea].append(chi)
    while pea != 1:
        pea = nodes[pea][0]
        nodes[pea].append(chi)
        
for i in range(q):
    p, q = map(int, input().split())
    if len(nodes[p]) != 1:
        for j in range(1,len(nodes[p])):
            counts[nodes[p][j]] += q
    counts[p] += q

str_counts = map(str, counts[1:])
print(' '.join(str_counts))
print(*counts[1:])
"""