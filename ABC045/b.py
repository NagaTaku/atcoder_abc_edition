a = input()
b = input()
c = input()

turn = "a"

while True:
    if turn == "a":
        if a =="":break
        turn = a[0]
        a = a[1:]
    if turn == "b":
        if b =="":break
        turn = b[0]
        b = b[1:]
    if turn == "c":
        if c =="":break
        turn = c[0]
        c = c[1:]

turn = turn.upper()
print(turn)