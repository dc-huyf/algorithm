class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        # 不要想太复杂了
        ## 记录价格最低点min_price
        ## 记录目前出现过的最大差价即可
        '''
        if len(prices) <= 1:
            return 0
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(price - min_price, max_profit)

        return max_profit

s = Solution()
s.maxProfit([2,7,1,4,11])