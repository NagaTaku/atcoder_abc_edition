n, x, t = map(int, input().split())
step = n//x
if n%x != 0:
    step += 1
print(step*t)