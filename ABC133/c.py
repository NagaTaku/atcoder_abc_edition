L, R = map(int, input().split())

MIN = 2018
if R-L > 4039:
    MIN = 0


MOD = 2019
L = L%MOD
R = R%MOD
if L > R:
    L, R = R, L
elif L == R:
    MIN = 0


for i in range(L, R):
    for j in range(i+1, R+1):
        buf = (i*j) % MOD
        #print(i, j)
        MIN = min(buf, MIN)

print(MIN)