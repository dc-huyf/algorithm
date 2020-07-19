class Solution:
    def kthSmallest(self, matrix, k: int):
        '''
        利用每行每列均是递增的特点
        '''
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left < right:
            mid = (right + left) // 2
            res = self.check_num(matrix, mid)
            if res >= k:
                right = mid
            else:
                left = mid + 1  # 这个地方要注意
        return left

    def check_num(self, matrix, num):
        col = 0
        row = len(matrix) - 1
        count = 0
        while row >= 0 and col <= len(matrix) - 1:
            if matrix[row][col] > num:
                row -= 1
            else:
                count += (row+1)
                col += 1
        return count


s = Solution()
s.kthSmallest(matrix = [[1,2],[1,3]], k = 3)


