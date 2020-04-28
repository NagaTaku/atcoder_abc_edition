h, w, n = map(int, input().split())

ans = [0]*10

a = []

if n != 0:
    for i in range(n):
        s = input()
        a.append(s)


for i in range(1,h-1):
    for j in range(1,w-1):
        s = 0
        for p in range(3):
            for q in range(3):
                st = str(i+p) + " " + str(j+q)
                if st in a:
                    s += 1
        if s == 0:
            ans[0] += 1
        else:
            ans[s] += 1

for i in range(10):
    print(ans[i])




f=lambda:map(int,input().split())
h,w,n=f()
d={}

while n:
 n-=1;x,y=f()
 for i in range(9):
     #タプルを作成、削除、追加、変更ができない複数のデータ管理の機能
     a=(x+i%3,y+i//3)
     #get(p,q)はkeyがpの要素を取り出し、存在しなかった場合の変数をqに設定する
     d[a]=d.get(a,0)+(h>=a[0]>2<a[1]<=w)

c=[list(d.values()).count(i+1)for i in range(9)]

print((h-2)*(w-2)-sum(c),*c)
