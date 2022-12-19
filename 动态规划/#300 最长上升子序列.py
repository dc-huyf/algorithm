from typing import List


class Solution:
    def __init__(self):
        self.res = None

    def lengthOfLIS(self, nums: List[int]) -> int:
        self.res = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    self.res[i] = max(self.res[i], 1+self.res[j])
        return max(self.res)

if __name__ == "__main__":
    s = Solution()
    res = s.lengthOfLIS([10,9,2,5,3,7,101,18])
    print(res)