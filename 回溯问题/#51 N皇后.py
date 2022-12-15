'''
## 初版代码
import copy
class Solution:
    def __init__(self):
        self.result = []

    def solveNQueens(self, n: int):
        track = [["." for _ in range(n)] for _ in range(n)]
        self.solve(n, track)
        return self.trans_X2point(self.result)

    def solve(self, n, track):
        # 设置终止条件
        if n == 0:
            return self.trans_track(track)
        target = 0
        for i in range(len(track)):
            for j in range(len(track[0])):
                if track[i][j] == ".":  # 表明该位置可填
                    target = 1
                    tmp = copy.deepcopy(track)
                    tmp = self.fill_pos(i, j, tmp)
                    res = self.solve(n-1, tmp)
                    if res:
                        if res not in self.result:
                            self.result += [res]
                    else:
                        continue
        # 遍历完发现，没有可填的位置，则此路不通
        if n > 0 and target == 0:
            return False

    def fill_pos(self, i, j, track):
        for row in range(len(track)):
            for col in range(len(track)):
                # 填补同行
                if row == i:
                    track[i][col] = "X"
                # 填补同列
                if col == j:
                    track[row][j] = "X"
                # 填补左下至右上：
                if i - row == col - j:
                    track[row][col] = "X"
                if row - i == col - j:
                    track[row][col] = "X"
        track[i][j] = "Q"
        return track

    def trans_track(self, track):
        res = [0] * len(track)
        for idx, t in enumerate(track):
            res[idx] = "".join(t)
        return res

    def trans_X2point(self, result):
        for i in range(len(result)):
            for j in range(len(result[0])):
                result[i][j] = result[i][j].replace("X", ".")
        return result
'''


# 逐行遍历，减少时间复杂度，能够通过
import copy
class Solution:
    def __init__(self):
        self.result = []

    def solveNQueens(self, n: int):
        track = [["." for _ in range(n)] for _ in range(n)]
        self.solve_row(0, track)
        return self.trans_X2point(self.result)

    # 逐行遍历
    def solve_row(self, row, track):
        if row >= len(track):
            return self.trans_track(track)
        target = 0
        for col in range(len(track)):
            if self.check_valid(row, col, track):
                target = 1
                tmp = copy.deepcopy(track)
                tmp[row][col] = "Q"
                res = self.solve_row(row+1, tmp)
                if res:
                    if res not in self.result:
                        self.result += [res]
                else:
                    continue
        if target == 0:
            return False

    def check_valid(self, i, j, track):
        # 检查ij位置插入皇后是否有效, 上方，左上 右上
        for row in range(1, i+1):
            # print((i,j,row))
            if track[i-row][j] == "Q":
                return False
            if j >= row and track[i-row][j-row] == "Q":
                return False
            if j + row < len(track) and track[i-row][j+row] == "Q":
                return False
        return True

    def trans_track(self, track):
        res = [0] * len(track)
        for idx, t in enumerate(track):
            res[idx] = "".join(t)
        return res

    def trans_X2point(self, result):
        for i in range(len(result)):
            for j in range(len(result[0])):
                result[i][j] = result[i][j].replace("X", ".")
        return result

s = Solution()
s.solveNQueens(4)
