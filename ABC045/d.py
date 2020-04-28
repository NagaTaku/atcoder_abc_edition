#部分点

h, w, n = map(int, input().split())

hako = [[0 for i in range(w)] for j in range(h)]
ans = [0]*10

#print("hako1 = {0}".format(hako))

if n != 0:
    print('a')
    for i in range(n):
        s, t = map(int, input().split())
        hako[s-1][t-1] = 1

#print("hako2 = {0}".format(hako))

for i in range(h-2):
    for j in range(w-2):
        s = 0
        for p in range(3):
            for q in range(3):
                if hako[i+p][j+q] == 1:
                    s += 1
        ans[s] += 1

for i in range(10):
    print(ans[i])
