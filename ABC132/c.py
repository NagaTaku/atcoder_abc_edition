N = int(input())
d = list(map(int, input().split()))

d.sort()

half = int(N/2)
print(d[half]-d[half-1])