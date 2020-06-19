n = int(input())
a = list(map(int, input().split()))
#b = set(i for i in range(n))
ans = [0]*n
warizai_index = set()

for i in range(n):
    for wari in warizai_index:
        if a[i]%a[wari] == 0 and i != wari:
            ans[i] = 1
            if i in warizai_index:
                warizai_index.remove(i)
            #if i in b:
            #    b.remove(i)
            break
    if ans[i] == 1:
        continue
    
    #for j in b:
    for j in range(i+1,n):
        if i == j:
            continue
        if a[i]%a[j] == 0:
            ans[i] = 1
            if i in warizai_index and a[i] != a[j]:
                warizai_index.remove(i)
            #if i in b:
            #    b.remove(i)
            warizai_index.add(j)
            break

print(ans.count(0))
