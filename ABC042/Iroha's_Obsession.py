# -*-coding: utf-8 -*-

#金額と個数の入力
sum,num = map(int,input().split())
#嫌いな数字の入力
dis = list(map(int,input().split()))

pay = sum #支払い金額
#1ずつ支払い金額を足して嫌いな文字が含まれていないか確認
while True:
  flag = 0 #嫌いな文字が含まれているか
  str_pay = str(pay)
  for i in str_pay:
    if int(i) in dis:
      flag = 1
      break
  if flag == 0:
    break
  else:
    pay = pay + 1
print(pay)