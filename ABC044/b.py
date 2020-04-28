s = input()

res = 'Yes'

for i in range(len(s)):
    hantei = s.count(s[i])
    if hantei%2 == 1:
        res = 'No'
        break

print(res)