import copy

n, k = map(int, input().split())
A = list(map(int, input().split()))

for p in range(k):
    B = [0]*n
    for i in range(n):
        if A[i] > 0:
            B[i] += 1
            for j in range(1, A[i]+1):
                if i-j >= 0:
                    B[i-j] += 1
                if i+j < n:
                    B[i+j] += 1

    A = copy.copy(B)

for i in A:
    print(i, end=' ')
print('')