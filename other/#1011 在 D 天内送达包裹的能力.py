class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        left = max(weights)
        right = sum(weights) + 1
        while left < right:
            middle = left + (right - left) // 2
            res = self.judge(weights, middle, D)
            if res:
                right = middle
            else:
                left = middle + 1
        return left

    def judge(self, weights, n, D):
        s = 0
        for i in range(len(weights)):
            s += weights[i]
            if s > n:
                D -= 1
                s = weights[i]
        if s > 0: D -= 1
        return D >= 0

s = Solution()
s.shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], D = 5)