w, h, n = map(int, input().split())

xmin, xmax, ymin, ymax = 0,w,0,h

for i in range(n):
    xi,yi,ai = map(int, input().split())
    if ai == 1:
        if xmin < xi:
            xmin = xi
    if ai == 2:
        if xmax > xi:
            xmax = xi
    if ai == 3:
        if ymin < yi:
            ymin = yi
    if ai == 4:
        if ymax > yi:
            ymax = yi

if xmax < xmin or ymax < ymin:
    menseki = 0
else:
    menseki = (xmax-xmin) * (ymax-ymin)
print(menseki)