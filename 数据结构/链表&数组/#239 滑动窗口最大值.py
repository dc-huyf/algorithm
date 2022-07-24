# 定义单调队列
class MonotonicQueue:
    def __init__(self):
        self.maxq = []

    def push(self, num):
        while len(self.maxq) > 0 and self.maxq[-1] < num:
            self.maxq.pop()
        self.maxq.append(num)

    def getMax(self):
        return self.maxq[0]

    def pop(self, n):
        if n == self.maxq[0]:
            self.maxq.pop(0)


class Solution:
    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        window = MonotonicQueue()
        res = []
        for i in range(len(nums)):
            if i < k-1:
                window.push(nums[i])
            else:
                window.push(nums[i])
                res.append(window.getMax())
                window.pop(nums[i-k+1])
        return res

if __name__ == "__main__":
    nums, k = [-1,0,3,5,9,12], 3
    s = Solution()
    print(s.maxSlidingWindow(nums, k))
