class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        # 动态规划解法
        '''
        if n <= 2:
            return n
        dp = [0 for _ in range(n)]
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

    def climbStairs2(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n+1):
            a, b = b, a+b
        return b

s = Solution()
s.climbStairs2(10)