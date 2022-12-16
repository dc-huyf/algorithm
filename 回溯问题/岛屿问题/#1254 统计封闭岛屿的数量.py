
class SolutionDFS(object):
    def __init__(self):
        self.res = 0
        self.grid = None
        self.m = None
        self.n = None
        self.steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def closedIsland(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.res = 0
        # 把靠边岛屿都淹了
        for i in range(self.m):
            if self.grid[i][0] == 0:
                self.dfs(i, 0)
            if self.grid[i][-1] == 0:
                self.dfs(i, self.n-1)
        for j in range(self.n):
            if self.grid[0][j] == 0:
                self.dfs(0, j)
            if self.grid[-1][j] == 0:
                self.dfs(self.m-1, j)

        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 0:
                    self.res += 1
                    self.dfs(i, j)
        return self.res

    def dfs(self, x, y):
        # 先把当前区域淹掉
        self.grid[x][y] = 1
        for a, b in self.steps:
            if x+a >= 0 and x+a < self.m and y+b >= 0 and y+b < self.n and self.grid[x+a][y+b] == 0:
                self.dfs(x+a, y+b)