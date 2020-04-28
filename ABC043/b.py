#文字列の入力
s = input()

f = ''

for i in s:
    if i == '0' or i == '1':
        f += i
    elif i == 'B':
        f = f[:-1]
    else:
        continue

print(f)