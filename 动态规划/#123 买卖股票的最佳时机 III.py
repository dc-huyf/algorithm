# 改造：进一步简化
# 状态：0 1
# 选择：买/卖/rest
class Solution:
    def maxProfit(self, prices) -> int:
        # 每天的状态都是一个 K * 2维矩阵
        # 初始化：卖出时记一次操作
        if len(prices) <= 1:
            return 0
        K = 2
        today = [[0, -prices[0]]] # 第一天
        for k in range(1, K+1):
            today.append([-float("inf"), -float("inf")])
        for idx in range(1, len(prices)):
            for k in range(K+1):
                if k == 0:
                    a = 0
                    b = max(today[0][1], -prices[idx])
                else:
                    a = max(today[k - 1][1] + prices[idx], today[k][0])
                    b = max(today[k][0] - prices[idx], today[k][1])
                today[k] = [a, b]
        return sorted(today, key=lambda x: x[0])[-1][0]

s = Solution()
s.maxProfit([1,2,3,4,5])