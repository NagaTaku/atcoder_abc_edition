import numpy as np

PI = 3.141592
P = 3.141592653589793238462643383279502884197169399
A, B, H, M = map(int, input().split())

A_ang = (30*H) + (0.5*M)
B_ang = 6 * M

angle = abs(A_ang - B_ang)
if angle > 180:
    angle = 360-angle

angle = (angle/360) * 2*P

a = (A*A) + (B*B) - (2*A*B*np.cos(angle))

a = np.sqrt(a)
print(a)
