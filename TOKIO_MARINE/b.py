oni_x, oni_speed = map(int, input().split())
chi_x, chi_speed = map(int, input().split())
time = int(input())
ans = False


if oni_speed > chi_speed:
    sa = abs(oni_x - chi_x)
    sa_speed = oni_speed - chi_speed
    if sa_speed*time >= sa:
        ans = True

if ans:
    print('YES')
else:
    print('NO')