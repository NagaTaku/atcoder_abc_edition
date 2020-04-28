# -*-coding: utf-8 -*-

#整数の入力
a = list(map(int, input().split()))
total = 0

for i in a:
  if i == 5 or i == 7:
  	total = total + i

if total == 17:
  print("YES")
else:
  print("NO")