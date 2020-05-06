s = input()

s_len = len(s)

for i in range(1, int(s_len/2)+1):
    s = s[:-2]
    half = int(len(s)/2)
    s_mae = s[:half]
    s_ato = s[half:]
    if s_mae == s_ato:
        break

print(len(s))