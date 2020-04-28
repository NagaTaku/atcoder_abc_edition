#最短経路探索
#ダイクストラ法よりも時間がかかるが、今回の場合は使用可能
#各頂点を繋ぐ辺よりも距離の短い迂回路があればその値を最短経路にする

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

##############################
n,w = map(int,input().split()) #n:頂点数　w:辺の数

d = [[float("inf")]*n for i in range(n)] 
#d[u][v] : 辺uvのコスト(存在しないときはinf)
x = [0]*w
y = [0]*w
z = [0]*w
for i in range(w):
    x[i],y[i],z[i] = map(int,input().split())
    d[x[i]-1][y[i]-1] = z[i]
    d[y[i]-1][x[i]-1] = z[i]
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０
d = warshall_floyd(d)

res = 0
for i in range(w):
    if z[i] > d[x[i]-1][y[i]-1]:
        res += 1
print(res)

"""""""""""""""""""""""""""""
import sys

def initialize_graph(m):
    graph = {}
    for i in range(m):
        a, b, c = map(int, input().split())
        graph = set_new_nodes(graph, a, b)
        graph[a][b] = c
        graph[b][a] = c
    return graph

def set_new_nodes(graph, a, b):
    if not a in graph.keys():
        graph[a] = {}
    if not b in graph.keys():
        graph[b] = {}
    return graph

def main():
    n,m = map(int, input().split())
    graph = initialize_graph(m)
    print(graph)
    print(n)


if __name__ == '__main__':
    main()
    sys.exit(0)
"""""""""""""""""""""""""""""