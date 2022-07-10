
class Solution:
    def kthSmallest(self, matrix, k: int):
        row, col = len(matrix), len(matrix[0])
        def count_num(num):
            i, j, c1, c2 = row - 1, 0, 0, 0
            while i >= 0 and j <= col - 1:
                if matrix[i][j] < num:
                    c1 += (i + 1)
                    j += 1
                elif matrix[i][j] == num: # 检查有几个是相等的
                    r = i
                    while r >= 0:
                        if matrix[r][j] == num:
                            c2 += 1
                        else:
                            c1 += (r + 1)
                            break
                        r -= 1
                    j += 1
                else:
                    i -= 1
            return c1, c2

        left = matrix[0][0]
        right = matrix[-1][-1]
        while left <= right:
            middle = (left + right) // 2
            c1, c2 = count_num(middle)
            if c1 < k and c1 + c2 >= k:   # c1：小于num的数量，c2：等于num的数量
                return middle
            elif c1 >= k:
                right = middle - 1
            else:
                left = middle + 1
        return left - 1





