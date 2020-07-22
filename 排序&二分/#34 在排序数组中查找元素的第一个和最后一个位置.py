class Solution:
    def searchRange(self, nums, target: int):
        # 左侧搜索
        left = 0
        right = len(nums)
        res = []
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        if left == len(nums) or nums[left] != target: # 数组中不存在target
            return [-1,-1]

        res.append(left)

        # 右侧搜索
        left = 0
        right = len(nums)
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        res.append(right - 1)
        return res

s = Solution()
s.searchRange(nums = [5,7,7,8,10], target = 11)


