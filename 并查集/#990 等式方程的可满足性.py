class DSU(object):
    def __init__(self, N):
        self.par = list(range(N))
        self.size = [1] * N
    def find(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return
        if self.size[xr] > self.size[yr]:
            self.par[yr] = xr
            self.size[xr] += self.size[yr]
        else:
            self.par[xr] = yr
            self.size[yr] += self.size[xr]
    def connect(self, p, q):
        return self.find(p) == self.find(q)


class Solution:
    def equationsPossible(self, equations) -> bool:
        # 先统计一下有多少字母
        if len(equations) < 1:
            return True
        chars = set(list("".join(equations).replace("=", "").replace("!", "")))
        chars2id = {c: id for c, id in zip(chars, range(len(chars)))}
        dsu = DSU(len(chars))
        # 准备合并
        for e in equations:
            if '==' in e:
                dsu.union(chars2id[e[0]], chars2id[e[-1]])
        # 重新检查
        for e in equations:
            res = dsu.connect(chars2id[e[0]], chars2id[e[-1]])
            if '==' in e:
                if not res:
                    return False
            else:
                if res:
                    return False
        return True


s = Solution()
print(s.equationsPossible(["a!=a"]))

