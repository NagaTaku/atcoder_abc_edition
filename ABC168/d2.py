import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix

N, M = map(int, input().split())

route_list = np.array([[0 for i in range(N)] for j in range(N)])

for i in range(M):
    a,b = map(int, input().split())
    route_list[a-1][b-1] = 1
    route_list[b-1][a-1] = 1
