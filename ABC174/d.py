n = int(input())
c = list(input())
r = c.count('R')

left = c[:r]    
ans = left.count('W')

print(ans)