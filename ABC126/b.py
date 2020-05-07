s = input()

n = 4

mae = int(s[:2])
ato = int(s[2:])

if mae < 13 and mae > 0:
    if ato < 13 and ato > 0:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if ato < 13 and ato > 0:
        print("YYMM")
    else:
        print("NA")