o = input()
e = input()

ans = ""
for i in range(len(o)-1):
    ans = ans + o[i] + e[i]


if (len(o) == len(e)):
    ans = ans + o[len(o)-1] + e[len(e)-1]
else:
    ans = ans + o[len(o)-1]

print(ans)

