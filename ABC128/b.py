n = int(input())

score = {}

for i in range(n):
    s, p = input().split()

    if s not in score:
        score[s] = []

    t = [i+1,int(p)]
    score[s].append(t)

city = sorted(score)
for key in city:
    score[key] = sorted(score[key], key=lambda x: x[1], reverse=True)

    for i in range(len(score[key])):
        print(score[key][i][0])
    
