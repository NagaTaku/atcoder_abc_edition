def iter_p_adic(p, n):
    '''
    連続して増加するp進数をリストとして返す。nはリストの長さ
    return
    ----------
    所望のp進数リストを次々返してくれるiterator
    '''
    from itertools import product
    tmp = [range(p+1)] * n
    return product(*tmp)


N, M, Q = map(int, input().split())

a, b, c, d = [], [], [], []
for i in range(Q):
    A, B, C, D = map(int, input().split())
    a.append(A)
    b.append(B)
    c.append(C)
    d.append(D)

MAX = 0
iterator = iter_p_adic(M,N)
for idxs in iterator:
    f = 0
    #print(idxs)
    A = list(idxs)
    A = sorted(A)
    for i in range(N):
        if A[i] == 0:
            f = 1
            break
    if f == 1:
        continue
    total = 0
    for i in range(Q):
        if c[i] == A[b[i]-1] - A[a[i]-1]:
            total += d[i]
    
    MAX = max(MAX, total)

print(MAX)







"""
for i in range(N):
    for j in range(M):
        A[i] 



A = [1]*N
for i in range(N):
    for j in range(i,M+1):
    


for i in range(1,M+1):
    for j in range(i,M+1):
        for p in range(j,M+1):
            for q in range(p,M+1):

3:4 20
2:4 10
4:2 5
5:2 6
3:3 10
"""