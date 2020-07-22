'''
深度优先搜索：DFS
从某一个1开始，"探索"每个区域
'''
class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.DFS(grid, i, j)
        return count
    def DFS(self, grid, x, y):
        grid[x][y] = 'X'
        m = len(grid)
        n = len(grid[0])
        steps = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        for step in steps:
            new_x = x + step[0]
            new_y = y + step[1]
            if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n:
                if grid[new_x][new_y] == '1':
                    self.DFS(grid, new_x, new_y)



'''
并查集，找最后的连通区域数量 - '0'的数量
'''
class DSU(object):
    def __init__(self, N):
        self.par = list(range(N))
        self.count = N
        self.size = [1] * N

    # 在寻找父结点的过程中压缩状态
    def find(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    # 合并两个结点
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
        self.count -= 1
        return True

    def connect(self, p, q):
        return self.find(p) == self.find(q)

    def Count(self):
        return self.count

class Solution1:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        dsu = DSU(m * n) # 定义类
        ## 遍历所有的'1'
        zero_num = 0
        steps = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for step in steps:
                        new_x = i + step[0]
                        new_y = j + step[1]
                        if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n:
                            if grid[new_x][new_y] == '1':
                                dsu.union(i * n + j, new_x * n + new_y)
                else:
                    zero_num += 1
        # 最后连通区域数量减去'0'的数量
        # print(dsu.Count())
        return dsu.Count() - zero_num

s = Solution1()
grid = [
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','1'],
['0','0','0','1','0']
]

s.numIslands(grid)


