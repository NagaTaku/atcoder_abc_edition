n = int(input())
k = int(input())
x = int(input())
y = int(input())

sum = 0

if n <= k:
    sum = n*x
elif n > k:
    sum = k*x + (n-k)*y

print(sum)
