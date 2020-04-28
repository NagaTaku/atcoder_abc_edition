# -*-coding: utf-8 -*-

#文字列の数、文字数の入力
num,len = map(int, input().split())
#文字列の入力
str = list(input() for i in range(num))
last_str = ""

str.sort() #ソート
#文字列の合体
for s in str:
  last_str = last_str + s
print(last_str)