#後ろから調査しましょう

s = input()

num = len(s)

while len(s)>=5:
    if s[-5:] == "dream" or s[-5:] == "erase":
        s = s[:-5]
    elif s[-7:] == "dreamer":
        s = s[:-7]
    elif s[-6:] == "eraser":
        s = s[:-6]
    else:
        break

if len(s) == 0:
    print('YES')
else:
    print('NO')