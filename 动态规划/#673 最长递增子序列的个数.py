class Solution:
    def findNumberOfLIS(self, nums) -> int:
        '''
        思路：dp[i] : nums[i]处的最长递增子序列长度 (length, count)
        两个目标： 1. 求出每个位置的最长递增子序列长度 2. 统计每个位置最长递增子序列个数
        '''
        if len(nums) <= 1 or len(set(nums)) == 1:
            return len(nums)
        dp = [[1, 1] for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]
                    else:
                        pass
        dp = sorted(dp, key = lambda x:x[0])
        result = 0
        for r in dp:
            if r[0] == dp[-1][0]:
                result += r[1]
        return result

s = Solution()
s.findNumberOfLIS([1,1,1,2,2,2,3,3,3])