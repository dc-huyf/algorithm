def maxSubArray(nums):
    '''
    dp[i]: 代表若以nums[i]为结尾，最大的自序和
    对于nums[i]：若dp[i-1]为负，则没有必要接着续，另起一个新的子序即可
    '''
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1], 0) + nums[i]
    return max(dp)