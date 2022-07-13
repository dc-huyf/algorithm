'''空间换时间的做法，时间复杂度O(1)
把问题转换为：求(i, j) -> (0, 0)元素和的问题，这个思路也比较巧妙
另外，求解过程中，稍稍注意下索引越界问题'''


class NumMatrix:

    def __init__(self, matrix: [[int]]):
        self.matrix = matrix
        self.res = [[0 for i in range(len(matrix[0])+1)] for j in range(len(matrix)+1)]
        # 遍历一下矩阵，计算（i,j) -> (0,0)区域的和
        for i in range(len(matrix)): # 先遍历行，再遍历列
            for j in range(len(matrix[0])):
                if i == 0 and j == 0:
                    self.res[i+1][j+1] = matrix[i][j]
                    continue
                if i == 0:
                    self.res[i+1][j+1] = self.res[i+1][j] + matrix[i][j]
                    continue
                if j == 0:
                    self.res[i+1][j+1] = self.res[i][j+1] + matrix[i][j]
                    continue
                self.res[i+1][j+1] = self.res[i][j+1] + self.res[i+1][j] - self.res[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.res[row2+1][col2+1] - self.res[row1][col2+1] - self.res[row2+1][col1] + self.res[row1][col1]


if __name__ == "__main__":
    matrix = [[1,0,0,1,4], [1,0,0,1,4], [1,0,0,1,4], [1,0,0,1,4]]
    row1, col1, row2, col2 = 0, 0, 3, 3
    obj = NumMatrix(matrix)
    param_1 = obj.sumRegion(row1,col1,row2,col2)
    print(param_1)