n = int(input())

s = []

for i in range(n):
    s.append(int(input()))

s = sorted(s)

total = 0
for i in range(n):
    total += s[i]

i = 0
while total > 0 and total%10 == 0:
    total -= s[i]
    i += 1

print(total)