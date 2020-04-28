#Union-Find木の問題
#グループ分けを木構造で管理するデータ構造のこと．
#同じグループに属する＝同じ木に属するという木構造でグループ分けをする際，
#以下の二点を高速で行うことができるのがメリット．


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

n, k, l = map(int, input().split())

ar = UnionFind(n)
br = UnionFind(n)
ans = [0]*n

#print(ar.parents)

for i in range(k):
    p, q = map(int, input().split())
    ar.union(p-1,q-1)

for i in range(l):
    p, q = map(int, input().split())
    br.union(p-1,q-1)

for i in range(n):
    s = set(ar.members(i)) & set(br.members(i))
    ans[i] = len(s)
    print(len(s), end=" ")

#for i in range(n):
#    pritn(ans[i])