a,b,c = map(int, input().split())

if a == b and b == c:
    print(str(1))
elif (a == b and a != c) or (a == c and a != b) or (a != b and b == c):
    print(str(2))
elif a != b and b != c and a != c:
    print(str(3))