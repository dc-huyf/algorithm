#
# 简单变相
# @param n int整型
# @param m int整型
# @param x int整型一维数组
# @param y int整型一维数组
# @return int整型
#
# class Solution:
#     def solve(self, n, m, x, y):
#         # write code here
#         # 从[1,1]出发，向右 斜上右方 斜下右方
#         dp = [[0 for _ in range(n)] for _ in range(3)]
#         dp[0][0] = 1
#         # 初始化路障
#         for i in range(m):
#             dp[x[i]-1][y[i]-1] = -1
#
#         for j in range(1, n):
#             if dp[0][j] != -1:
#                 dp[0][j] += (0 if dp[0][j-1] == -1 else dp[0][j-1])
#                 dp[0][j] += (0 if dp[1][j-1] == -1 else dp[1][j-1])
#             if dp[2][j] != -1:
#                 dp[2][j] += (0 if dp[2][j-1] == -1 else dp[2][j-1])
#                 dp[2][j] += (0 if dp[1][j-1] == -1 else dp[1][j-1])
#             if dp[1][j] != -1:
#                 dp[1][j] += (0 if dp[1][j-1] == -1 else dp[1][j-1])
#                 dp[1][j] += (0 if dp[2][j-1] == -1 else dp[2][j-1])
#                 dp[1][j] += (0 if dp[0][j-1] == -1 else dp[0][j-1])
#
#         return dp[-1][-1] % (1000000007)
#
# s = Solution()
# s.solve(350,35,[3,3,3,1,1,2,1,2,2,3,3,1,3,1,3,1,2,3,3,2,1,3,3,1,1,2,1,1,2,1,2,2,3,3,3],[302,47,85,8,13,1,329,239,31,231,57,343,87,241,199,15,57,279,246,33,163,57,79,284,315,91,236,345,101,235,288,110,200,32,249])


class Solution:
    def WordsMerge(self, Words):
        # write code here
        record = []
        if not Words:
            return ""

        for word in Words:
            if record:
                l = 0
                while word[l] == record[-1] and l < len(word):
                    record.pop()
                    l += 1
                    if len(record) == 0:
                        break
                record += list(word[l:])
            else:
                record += list(word)
        return "".join(record)

s = Solution()
s.WordsMerge(["aab","bac","ccd"])