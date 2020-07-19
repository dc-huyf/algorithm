class Solution:
    def searchMatrix(self, matrix, target):
        ## 从左下角开始搜索，matrix[i][j] > target,则向上, 反之则向右
        if not matrix or not len(matrix[0]):
            return False
        col = 0
        row = len(matrix) - 1
        while row >= 0 and col <= len(matrix[0]) - 1:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
        return False

s = Solution()
s.searchMatrix([[-1, 3]], 3)




