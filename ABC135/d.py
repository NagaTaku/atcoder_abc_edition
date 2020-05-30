S = input()

list_s = list(S)
length = len(list_s)
Min = int(S.replace('?', '0'))
idx = [length-i-1 for i, x in enumerate(list_s) if x == '?']

print(idx)
