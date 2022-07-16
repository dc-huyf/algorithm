class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        l, r = self.left_bound(nums, target), self.right_bound(nums, target)
        return [l, r]

    def left_bound(self, nums, target):
        start, end = 0, len(nums)-1 # 在[start, end]内搜索
        while start <= end: # start > end结束,注意保证能够结束循环
            mid = (start + end) // 2
            if nums[mid] == target:
                end = mid - 1 # 搜索[start, mid-1]
            if nums[mid] > target:
                end = mid - 1 # 搜索[start, mid-1]
            if nums[mid] < target:
                start = mid + 1 # 搜索[mid+1, end]
        if start >= len(nums):
            return -1
        return start if nums[start]==target else -1

    def right_bound(self, nums, target):
        start, end = 0, len(nums) - 1  # 在[start, end]内搜索
        while start <= end:  # start > end结束,注意保证能够结束循环
            mid = (start + end) // 2
            if nums[mid] == target:
                start = mid + 1  # 增大左边界，搜索[mid+1, end]
            if nums[mid] > target:
                end = mid - 1  # 搜索[start, mid-1]
            if nums[mid] < target:
                start = mid + 1  # 搜索[mid+1, end]
        if start == 0:
            return -1
        return end if nums[end] == target else -1


if __name__ == "__main__":
    nums, target = [5,7,7,8,8,10], 10
    s = Solution()
    print(s.searchRange(nums, target))