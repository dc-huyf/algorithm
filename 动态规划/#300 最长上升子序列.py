class Solution:
    def lengthOfLIS(self, nums) -> int:
        '''
        #  dp[i] = max(dp[i], dp[j] + 1) dp[j]为nums[j]比nums[i]小的
        '''
        if len(nums) == 0:
            return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

s = Solution()
s.lengthOfLIS([10,9,2,5,3,7,101,18])