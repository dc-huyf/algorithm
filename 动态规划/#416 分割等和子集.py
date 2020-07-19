import copy
# 反复copy时间太慢，并且思路比较繁琐
class Solution1:
    def canPartition(self, nums):
        target = sum(nums) // 2
        if target != sum(nums) / 2:
            return False
        # 若某元素已选，则不能再选
        ## target: [],记录凑够target后，剩余那些元素
        memo = {}
        for num in nums:
            # dp[num] = 1
            tmp = copy.deepcopy(nums)
            tmp.remove(num)
            memo[num] = tmp
        for i in range(1, target + 1):
            for num in nums:
                if i - num in memo.keys() and num in memo[i - num]:
                    tmp = copy.deepcopy(memo[i - num])
                    tmp.remove(num)
                    memo[i] = tmp
                    break
        return True if target in memo.keys() else False


'''
dp[N][target]：能否凑够target
选择：是否装nums[i]
值：False/True
'''
class Solution2:
    def canPartition(self, nums):
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        dp = [[False for _ in range(target+1)] for _ in range(len(nums)+1)]
        for i in range(len(dp)):
            dp[i][0] = True
        for i in range(1, len(nums)+1):
            for j in range(1, target+1):
                if j - nums[i-1] < 0: # 超出背包限制，没得选择，不能装入
                    dp[i][j] = dp[i-1][j]  # 代表不装入nums[i]
                else:
                    # 做选择，是否装入
                    dp[i][j] = dp[i-1][j - nums[i-1]] or dp[i-1][j]
        return dp[-1][-1]


# 基于solution2再进行一定优化，dp[i][j]仅和dp[i-1][:]有关，可以压缩状态
class Solution3:
    def canPartition(self, nums):
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        dp = [False for _ in range(target+1)]
        dp[0] = True
        i = 1
        while i <= len(nums):
            for j in range(target, -1, -1):
                if j - nums[i-1] >= 0:
                    # 做选择，是否装入
                    dp[j] = dp[j - nums[i-1]] or dp[j]
            i += 1
        return dp[-1]
s = Solution3()
s.canPartition([1, 2,5])