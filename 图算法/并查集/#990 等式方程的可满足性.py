from typing import List


class DSU(object):
    def __init__(self, N):
        self.parents = list(range(N+1))
        self.size = [1] * (N+1)

    def find(self, x):
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp == yp: return
        if self.size[xp] > self.size[yp]:
            self.parents[yp] = xp
            self.size[xp] += self.size[yp]
        else:
            self.parents[xp] = yp
            self.size[yp] += self.size[xp]

    def is_connect(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = DSU(26)
        # 先遍历== 再遍历!=

        not_equal_list = []
        for strs in equations:
            if strs[1] == "=":
                dsu.union(ord(strs[0])-ord("a"), ord(strs[-1])-ord("a"))
            else:
                not_equal_list.append([ord(strs[0])-ord("a"), ord(strs[-1])-ord("a")])

        # 逐一检验！=是否冲突
        for a, b in not_equal_list:
            ap, bp = dsu.find(a), dsu.find(b)
            if ap == bp:
                return False
        return True


s = Solution()
print(s.equationsPossible(["a!=a"]))

