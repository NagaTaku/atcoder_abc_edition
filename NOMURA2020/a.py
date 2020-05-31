h1, m1, h2, m2, k = map(int, input().split())

kisho = 60-m1
kisho += 60*(h2-h1-1) 
kisho += m2

ans = kisho-k

print(ans)