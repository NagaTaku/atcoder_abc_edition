n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0

# もしすべてaから選んだ場合
time = k
aOnly = 0
for i in range(len(a)):
    time -= a[i]
    if time < 0:
        time += a[i]
        i -= 1
        break
    aOnly += 1
a_idx = i
b_idx = -1

for i in range(len(b)):
    time -= b[i]
    if time < 0:
        time += b[i]
        i -= 1
        break
    aOnly += 1
b_idx = i
ans = aOnly

ans_kari = ans
for i in range(a_idx, -1, -1):
    time += a[i]
    ans_kari -= 1
    for j in range(b_idx+1, len(b)):
        time -= b[j]
        if time < 0:
            time += b[j]
            b_idx = j-1
            break
        ans_kari += 1
    ans = max(ans, ans_kari)
    
print(ans)