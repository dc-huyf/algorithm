class Solution:
    def rob(self, nums) -> int:
        '''
        首尾不能同时偷
        1. 首尾都不偷
        2. 偷首不偷尾
        3. 偷尾不偷首
        '''
        return max(self.solver(nums[1:-1]), self.solver(nums[:-1]), self.solver(nums[1:]))

    def solver(self, nums):
        if not nums:
            return 0
        a = nums[0]
        b = 0
        for i in range(1, len(nums)):
            a, b = b + nums[i], max(a, b)
        return max(a, b)

s = Solution()
s.solver([1,2,3,1])