import copy

N = int(input())
A = [0]*N
for i in range(N):
    A[i] = int(input())

MaxIndex = A.index(max(A))

for i in range(N):
    if i != MaxIndex:
        print(A[MaxIndex])
    else:
        B = copy.copy(A)
        del B[MaxIndex]
        print(max(B))
