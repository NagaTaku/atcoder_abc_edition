n, k = map(int, input().split())

a = list(map(int, input().split()))
done = [0]*n
stay = 1

for i in range(1, k+1):
    if done[stay-1] != 0:
        break
    done[stay-1] = i
    stay = a[stay-1]

nokori = k + 1 - i
if nokori != 1:
    loop = i - done[stay-1]
    for i in range(nokori%loop):
        stay = a[stay-1]

print(stay)
