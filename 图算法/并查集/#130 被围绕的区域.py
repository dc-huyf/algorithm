'''
思路一：DFS
先找出所有四条边上的'O',记为'#'
然后对'#'上下左右进行搜索，若为'O'则改为'#'

思路二：并查集
先找出所有四条边上的'O',与dummy连通
连通所有独立区域内的'O'
最后不与dummy连通的'O'均改为'#'
'''

class SolutionDFS:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ## 先检查左右两列
        if board:
            for i in range(len(board)):
                if board[i][0] == 'O':
                    self.DFS(board, i, 0)
                if board[i][-1] == 'O':
                    self.DFS(board, i, len(board[0]) - 1)
            for j in range(len(board[0])):
                if board[0][j] == 'O':
                    self.DFS(board, 0, j)
                if board[-1][j] == 'O':
                    self.DFS(board, len(board) - 1, j)

            # 遍历board
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 'O':
                        board[i][j] = 'X'
                    if board[i][j] == '#':
                        board[i][j] = 'O'

    def DFS(self, board, row, col):
        board[row][col] = '#'
        steps = [[0, 1], [0, -1], [-1, 0], [1, 0]] # 定义上下左右四个方向
        for step in steps:
            new_x, new_y = row + step[0], col + step[1]
            if new_x >= 0 and new_x <= len(board) - 1 and new_y >= 0 and new_y <= len(board[0]) - 1:
                if board[new_x][new_y] == 'O':
                    self.DFS(board, new_x, new_y)

class DSU(object):
    def __init__(self, N):
        self.par = list(range(N + 1))
        self.size = [1] * (N + 1)
        self.count = N + 1
    def find(self, x):
        while self.par[x] != x:
            # 状态压缩
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    # 比较两树体量进行合并
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        elif self.size[xr] < self.size[yr]:
            self.par[xr] = yr
            self.size[yr] += self.size[xr]
        else:
            self.par[yr] = xr
            self.size[xr] += self.size[yr]
        self.count -= 1
        return True

    def connect(self, p, q):
        rp = self.find(p)
        rq = self.find(q)
        return rp == rq

    # 返回连通分量的个数
    def count(self):
        return self.count

class SolutionDSU:
    def solve(self, board) -> None:
        ## 特殊情形
        if not board:
            return
        ## 创建数组，长度维m * n
        m = len(board)
        n = len(board[0])
        # 创建并查集
        dsu = DSU(m * n + 1)
        dummy = m * n

        ## 将暴露在外的'O'与dummy连接
        for i in range(m):
            if board[i][0] == 'O':
                dsu.union(i * n, dummy)
            if board[i][-1] == 'O':
                dsu.union((i+1) * n - 1, dummy)
        for j in range(n):
            if board[0][j] == 'O':
                dsu.union(j, dummy)
            if board[-1][j] == 'O':
                dsu.union((m-1) * n + j, dummy)
        ## 上下左右移动
        steps = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        # 连通一起的'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    for step in steps:
                        x, y = i + step[0], j + step[1]
                        if x >= 0 and x < m and y >= 0 and y < n:
                            if board[x][y] == 'O':
                                dsu.union(i * n + j, x * n + y)
        ## 查找所有不跟dummy连通的'O'
        for i in range(1, m-1):
            for j in range(1, n-1):
                if not dsu.connect(dummy, i*n+j):
                    board[i][j] = 'X'

if __name__ == "__main__":
    s = SolutionDFS()
    board = [["X","O","X"],
             ["O","X","O"],
             ["X","O","X"]]
    res = s.solve(board)
    print(res)







