class Solution1:
    def rob(self, nums) -> int:
        '''
        # 状态：截止第i户人家，偷的最大金额
        # 选择：偷/不偷
        dp[i] = [,]
        dp[i][0] = dp[i-1][1] + nums[i]
        dp[i][1] = max(dp[i-1][1], dp[i-1][0])
        '''
        if not nums:
            return 0
        dp = [[] for _ in range(len(nums))]
        dp[0] = [nums[0], 0]
        for i in range(1, len(nums)):
            dp[i] = [dp[i-1][1] + nums[i], max(dp[i-1][1], dp[i-1][0])]
        return max(dp[-1])


## 进一步简化
class Solution1:
    def rob(self, nums) -> int:
        if not nums:
            return 0
        a = nums[0]
        b = 0
        for i in range(1, len(nums)):
            a, b = b + nums[i], max(a, b)
        return max(a, b)
