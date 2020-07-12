class Solution:
    def maxProfit(self, prices) -> int:
        # 理清楚什么是状态，什么是选择
        # 状态：是否持有、目前交易次数、当前天数
        # 三种可能的选择：buy sell rest
        '''
        第i天的结果是并未持有股票，则两种选择为今天抛出/rest: dp[i][k][0] = max(dp[i-1][k-1][1] + prices[i], dp[i-1][k][0])
        第i天的结果是持有股票，则两种选择为今天买入/rest: dp[i][k][1] = max(dp[i-1][k][0] - prices[i], dp[i-1][k][1])
        优化：当天的状态仅仅和前一天有关，不需要存储每天的状态, 使用a表示未持有， b表示持有股票的状态值
        '''
        if len(prices) <= 1:
            return 0
        a = 0
        b = -prices[0]
        for idx, price in enumerate(prices):
            if idx != 0:
                a, b = max(b + price, a), max(a - price, b)
        return a

s = Solution()
s.maxProfit([7,1,5,3,6,4])