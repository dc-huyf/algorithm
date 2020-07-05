class Solution:
    def minEatingSpeed(self, piles, H: int) -> int:
        # 二分查找
        left = 0
        right = sum(piles)
        while left < right:
            if right == 1:
                return 1
            middle = left + (right - left) // 2
            res = self.judge(piles, middle, H)
            if res:
                right = middle
            else:
                left = middle + 1
        return left

    def judge(self, piles, n, H):
        for i in piles:
            H -= i // n
            if i % n > 0:
                H -= 1
        return H >= 0

s = Solution()
s.minEatingSpeed([312884470], 968709470)