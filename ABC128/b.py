n = int(input())

score = {}

for i in range(n):
    s, p = input().split()

    if s in score.keys:
        score[s].appenc(int(p))
    else:
        score[s] = list(int(p))

print(score)