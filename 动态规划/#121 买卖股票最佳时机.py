class Solution1:
    def maxProfit(self, prices) -> int:
        '''
        1. 简单问题简单解决
        '''
        if len(prices) <= 1:
            return 0
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(price - min_price, max_profit)
        return max_profit

class Solution2:
    def maxProfit(self, prices) -> int:
        '''
        动态规划问题：dp[i] = [min_buy, profit]
        dp[i][0] = min(price, dp[i-1][0])
        dp[i][1] = max(dp[i-1][1], price - dp[i][0])
        '''
        if len(prices) <= 1:
            return 0
        dp = [[] for _ in range(len(prices))]
        for idx, price in enumerate(prices):
            if idx == 0:
                dp[0] = dp[0] = [prices[0], 0]
                continue
            dp[idx].append(min(price, dp[idx-1][0]))
            dp[idx].append(max(dp[idx - 1][1], price - dp[idx][0]))
        return dp[-1][-1]

s = Solution2()
s.maxProfit([2,7,1,4,11])


