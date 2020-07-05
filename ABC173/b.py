N = int(input())
ans = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}

for i in range(N):
    s = input()
    ans[s] += 1

for key, value in ans.items():
    print(key + ' x ' + str(value))