s = input()

length = len(s)
f = 0

for p in range(length-1):
    for q in range(p+2,p+4):
        hikaku = s[p:q]
        #print(hikaku)
        for i in range(len(hikaku)):
            num = hikaku.count(hikaku[i])
            if num > len(hikaku)/2:
                print(str(p+1) + ' ' + str(q))
                f = 1
                break
        if f == 1:
            break
    if f == 1:
        break
if f == 0:
    print('-1 -1')
