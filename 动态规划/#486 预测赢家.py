class Solution:
    def PredictTheWinner(self, nums):
        '''
        若为偶数个，则一定存在一种策略能使得某个人必赢。那么谁是先手，谁就拥有选择权，就能赢
        若为奇数个，则有一定策略：
          - 前提条件：任何区间都存在最优策略：先手能够取得最大分数差
          - dp[i][j] : 代表nums[i:j+1]在最优策略下，先手取得的分数差
          - 在最优策略中，若玩家拿了i, 则nums[i+1, j+1]内也是最优策略
          - dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        '''
        if len(nums) % 2 == 0:
            return True
        dp = [[False for _ in range(len(nums))] for _ in range(len(nums))]
        # 搜索方式需要改一下，从对角线往右上角递推
        for i in range(len(nums)):
            dp[i][i] = nums[i]
        for row in range(1, len(nums)):
            for i in range(len(nums)):
                j = i + row
                if j < len(nums):
                    dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        # return dp
        if dp[0][-1] >= 0:
            return True
        else:
            return False

s = Solution()
s.PredictTheWinner([1,1,1])




