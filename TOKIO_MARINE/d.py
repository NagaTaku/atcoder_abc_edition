N = int(input())
V = [None]*N
W = [None]*N

for i in range(N):
    V[i], W[i] = map(int, input().split())

Q = int(input())

for q in range(Q):
    v, L = map(int, input().split())
    
    sosen = set()
    t = v
    while t != 1:
        sosen.add(t)
        t = int(t/2)
    sosen.add(1)
    sosen_list = list(sosen)
    dp = [[0]*(L+1) for i in range(len(sosen_list)+1)]

    for i in range(len(sosen_list)):
        for j in range(L+1):
            if j < W[sosen_list[i]-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-W[sosen_list[i]-1]]+V[sosen_list[i]-1])
    print(dp[-2][-1])
