N = int(input())
A = list(map(int, input().split()))
Q = int(input())
dic = dict()

for i in A:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

ans = 0
for num in dic:
    ans += num * dic[num]

for i in range(Q):
    b, c = list(map(int, input().split()))
    x = 0
    if b in dic:
        x = dic.pop(b)
        if c in dic:    
            dic[c] += x
        else:
            dic[c] = x
    ans += x * (c-b)
    print(ans)