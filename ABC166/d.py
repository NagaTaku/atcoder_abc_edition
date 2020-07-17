# 全探索でいける
# A**5 - B**5 = X　となるようなAとBの値
# -200~200の間の数値を計算すれば十分

x  = int(input())
ans = False

for a in range(-200,201):
    for b in range(-200, 201):
        if a**5 - b ** 5 == x:
            ans = True
            break
    if ans:
        break
print(a,b)