h, w, m = map(int, input().split())
bomber = [[0]*m for _ in range(m)]
bomb = {}
bomb2 = {}
ans = 0
MAX = 0
MAX_key = None

for i in range(m):
    mh, mw = map(int, input().split())
    bomber[mh-1][mw-1] = 1
    if mh in bomb:
        bomb[mh] += 1
    else:
        bomb[mh] = 1
    if mw in bomb2:
        bomb2[mw]+= 1
    else:
        bomb2[mw] = 1

max_kv_list_h = [kv for kv in bomb.items() if kv[1] == max(bomb.values())]
#print(max_kv_list_h)
#print(max_kv_list_h[0][0])

max_kv_list_w = [kv for kv in bomb2.items() if kv[1] == max(bomb2.values())]
#print(max_kv_list_w)

for i in range(len(max_kv_list_h)):
    for j in range(len(max_kv_list_w)):   
        if bomber[max_kv_list_h[i][0]-1][max_kv_list_w[j][0]-1] == 0:
            ans = max(max_kv_list_h[i][1]+max_kv_list_w[j][1], ans)
        else:
            ans = max(max_kv_list_h[i][1]+max_kv_list_w[j][1]-1, ans)


print(ans)

"""
dele = max(bomb, key=bomb.get)
num = bomb[dele]

bomb2 = {}
for i in range(m):
    if mh[i] == dele:
        continue
    if mw[i] in bomb2:
        bomb2[mw[i]] += 1
    else:
        bomb2[mw[i]] = 1
max_v = max(bomb2.values())
total = num + max_v
ans = max(ans, total)
"""
#print(ans)