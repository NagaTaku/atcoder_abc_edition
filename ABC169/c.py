"""
import math

A, B = map(float, input().split())
print(math.floor(A*B))
"""

#A, B = map(float, input().split())
s = input()
A = s.split()[0]
Q = int(A)
B = s.split()[1]
#B = float(B)
P = int(B[0])*100 + int(B[2])*10 + int(B[3])
T = Q*P
T = str(T)
ans = ''
if len(T)<3 or Q==0 or P==0:
    ans = '0'
else :
    ans = T[:-2]
print(ans)
