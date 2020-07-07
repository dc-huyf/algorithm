import copy
class Solution:
    def threeSum(self, nums):
        # 外层循环 + 内层双指针
        nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                return result
            # 跳过重复值
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < -nums[i]:
                    left += 1
                elif nums[left] + nums[right] == -nums[i]:
                    result.extend([[nums[i], nums[left], nums[right]]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
                    left += 1
                else:
                    right -= 1
        return result

s = Solution()
s.threeSum([-1, 0, 1, 2, -1, -4])
