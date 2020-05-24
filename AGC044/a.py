T = int(input())

ans = [0]*T

for i in range(T):
    N, A, B, C, D = map(int, input().split())
    total = 0
    money = 0
    while True:
        hikaku = [0.0 for i in range(4)]
        if total*5 <= N:
            hikaku[2] = float(4*total/C)
        if total*3 <= N:
            hikaku[1] = float(2*total/B)
        if total*2 <= N:
            hikaku[0] = float(total/A)
        
        hikaku[3] = float(1/D)
        maxIndex = [i for i, x in enumerate(hikaku) if x == max(hikaku)]
        if maxIndex[0] != 3:
            break
        else:
            total += 1
            money += D
        print(total, money)

    gosa = total

    while total <= N-gosa:
        hikaku = [0.0 for i in range(3)]
        if total*5 <= N+gosa:
            hikaku[2] = float(4*total/C)
        if total*3 <= N+gosa:
            hikaku[1] = float(2*total/B)
        if total*2 <= N+gosa:
            hikaku[0] = float(total/A)

        maxIndex = [i for i, x in enumerate(hikaku) if x == max(hikaku)]
        if maxIndex[0] == 0:
            total *= 2
            money += A
        elif maxIndex[0] == 1:
            total *= 3
            money += B
        elif maxIndex[0] == 2:
            total *= 5
            money += C
        print(total,money)
        
    money += D*(abs(N-total))

    print(money)
"""
1
11 1 2 4 8
"""