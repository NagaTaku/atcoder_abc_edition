x = int(input())

have = 100
year = 0

while have < x:
    year += 1
    have = int(have * 1.01)

print(year)