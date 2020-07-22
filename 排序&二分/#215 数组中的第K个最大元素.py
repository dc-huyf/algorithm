class Solution:
    def findKthLargest(self, nums, k):
        return sorted(nums)[-k]


# 插入排序，超时
class Solution:
    def findKthLargest(self, nums, k):
        for cur in range(len(nums)):
            curr = nums[cur]
            pre = cur - 1
            while pre >= 0 and nums[pre] > curr:
                nums[pre + 1] = nums[pre]
                pre -= 1
            nums[pre + 1] = curr
        return nums[-k]

# 归并可以通过
class Solution:
    def findKthLargest(self, nums, k):
        return self.main(nums)[-k]
    def main(self, nums):
        if len(nums) < 2:
            return nums
        left = nums[: len(nums) // 2]
        right = nums[len(nums) // 2: ]
        return self.merge(self.main(left), self.main(right))
    def merge(self, left, right):
        res = []
        while left and right:
            if left[-1] <= right[-1]:
                res.append(right.pop())
            else:
                res.append(left.pop())
        while left:
            res.append(left.pop())
        while right:
            res.append(right.pop())
        return res[::-1]


# 快排，按个人习惯，我常用最后一个元素作为比较基准
class Solution:
    def findKthLargest(self, nums, k):
        return self.main(nums)[-k]

    def main(self, nums):
        if len(nums) >= 2:
            base = nums.pop()
            left = []
            right = []
            for i in nums:
                if i <= base:
                    left.append(i)
                else:
                    right.append(i)
            return self.main(left) + [base] + self.main(right)
        else:
            return nums

s = Solution()
s.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4)
