n, q = map(int, input().split())
children = [0]*n
en = [-1]*(2*10**5)

for _ in range(n):
    children[i], b = map(int, input().split())
    en[b-1] = min(children[i], en[b-1])


    