'''
dp[i][j]:前i个元素能否组成j
选择就是：nums[i-1]是否选入
'''
class Solution:
    def change(self, amount: int, coins):
        if amount == 0:
            return 1
        coins = sorted(coins)
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for i in range(len(coins)):  # dp[i]
            for j in range(1, amount+1):  # dp[i][j]
                if j - coins[i] >= 0:  # 代表背包未满，coins[i]可以考虑选入背包
                    dp[j] += dp[j-coins[i]]
        return dp[-1]

s = Solution()
s.change(amount = 5, coins = [1, 2, 5])
