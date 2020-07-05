import copy

def nuri(is_tate, n, hako):
    if is_tate:
        for i in range(len(hako)):
            hako[i][n] = 'r'

    else:
        for i in range(len(hako[n-1])):
            hako[n][i] = 'r'
        

h, w, k = map(int, input().split())
ans = 0
c = []
for i in range(h):
    c.append(list(input()))

for i in range(2 ** (h+w)):
    c_ex = copy.deepcopy(c)
    for j in range(h+w):
        if ((i >> j) & 1):
            if j >= h:
                idx = j-h
                nuri(True, idx, c_ex)
            else:
                idx = j
                nuri(False, idx, c_ex)

    num = 0
    for j in range(len(c_ex)):
        num += c_ex[j].count('#')
    if num == k:
        ans += 1

print(ans)