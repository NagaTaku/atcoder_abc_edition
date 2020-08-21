n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = (-1)*float('inf')
done = [False]*n

for heiro_i in range(1, n+1):
    if not done[heiro_i-1]:
        now = heiro_i
        heiro = []
        while done[now-1] != True:
            done[now-1] = True
            heiro.append(now)
            now = p[now-1]
        
        if k > len(heiro):
            now = heiro[0]
            heiro_point = 0
            for i in range(len(heiro)):
                now = p[now-1]
                heiro_point += c[now-1]
            if heiro_point > 0:
                junkai_num = len(heiro)
                sho = k//junkai_num
                now_p = heiro_point*sho
            num = k%heiro
        else:
            now_p = 0
            num = k

        for i in range(len(heiro)):
            now = heiro[i]
            for j in range(num):
                now = p[now-1]
                num -= 1
                now_p += c[now-1]
                ans = max(ans, now_p)
print(ans)


"""
for start in range(1,n+1):
    now = start
    num = k
    now_p = 0
    for i in range(k):
        now = p[now-1]
        num -= 1
        now_p += c[now-1]
        ans = max(ans, now_p)

        if now == start:
            break
    if num > 0 and now_p > 0:
        junkai_num = k-num
        sho = num//junkai_num
        if sho != 0:
            now_p += now_p*sho
            num -= sho*junkai_num
        ans = max(ans, now_p)
        for i in range(num):
            now = p[now-1]
            num -= 1
            now_p += c[now-1]
            ans = max(ans, now_p)
print(ans)
"""