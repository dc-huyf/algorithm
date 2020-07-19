class Solution:
    def subarraySum(self, nums, k: int) -> int:
        ## sum(nums[:i]) - sum(nums[:j]) = k
        sum_dict= {}
        count = 0
        if len(nums) == 0:
            return 0
        sums = 0
        for i in range(1, len(nums) + 1):
            sums += nums[i-1]
            if sums == k: # 若num[:i]和为k，则直接计数
                count += 1
            if sum_dict.get(sums - k, 0) != 0:
                count += sum_dict[sums - k]
            sum_dict[sums] = sum_dict.get(sums, 0) + 1
        return count

s = Solution()
s.subarraySum(nums = [1], k = 1)
