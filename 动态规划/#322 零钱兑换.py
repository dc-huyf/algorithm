class Solution:
    def coinChange(self, coins, amount) -> int:
        '''
        背包问题：
        dp[i] : 代表凑成i,所需要的最少硬币数量
        dp[m] = min(dp[m - c] + 1, dp[m])
        '''
        if amount == 0:
            return 0
        dp = [float("inf") for _ in range(amount+1)]
        for i in coins:
            if i < amount + 1:
                dp[i] = 1
        for m in range(1, amount+1):
            for c in coins:
                if m - c >= min(coins) and dp[m-c] != float("inf"):
                    dp[m] = min(dp[m - c] + 1, dp[m])
        if dp[-1] != float("inf"):
            return dp[-1]
        else:
            return -1
s = Solution()
s.coinChange([1], 2)

