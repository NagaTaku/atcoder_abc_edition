n = int(input())
a = list(map(int, input().split()))

a = sorted(a)

print(a[n-1] - a[0])