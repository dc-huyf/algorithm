class Solution:
    def generateMatrix(self, n: int) -> [[int]]:

        matrix = [[0 for i in range(n)] for j in range(n)]
        left_up = [0, 0]
        right_down = [n-1, n-1]
        num = 1
        while left_up[0] < right_down[0] and left_up[1] < right_down[1]:
            # 上面一排
            for i in range(left_up[1], right_down[1]):
                matrix[left_up[0]][i] = num
                num += 1
            # 右面一排
            for i in range(left_up[0], right_down[0]):
                matrix[i][right_down[1]] = num
                num += 1
            # 下面一排
            for i in range(right_down[1], left_up[1], -1):
                matrix[right_down[0]][i] = num
                num += 1
            # 左边一排
            for i in range(right_down[0], left_up[0], -1):
                matrix[i][left_up[1]] = num
                num += 1

            # 更新坐标起终点
            left_up[0] += 1
            left_up[1] += 1
            right_down[0] -= 1
            right_down[1] -= 1

        if left_up == right_down:
            matrix[left_up[0]][left_up[1]] = num

        return matrix


if __name__ == "__main__":
    n = 1
    s = Solution()
    print(s.generateMatrix(n))