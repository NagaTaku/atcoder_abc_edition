k = int(input())
i = 0
t = 1
k = k*9

if k%7 == 0 :
    k = k/7
if k%2 == 0 or k%5 == 0:
    i = -1
else:
    while(True):
        t *= 10
        i += 1
        t = t%k
        if t==1:
            break
    
print(i)