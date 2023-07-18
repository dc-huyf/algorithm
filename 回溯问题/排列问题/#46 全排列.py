from typing import List


class Solution:
    def __init__(self):
        self.res = []
        self.nums = None

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.dfs([])
        return self.res

    def dfs(self, track):
        # 结束条件
        if len(track) == len(self.nums):
            self.res.append(track[:])
            return
        for idx in range(len(self.nums)):
            if self.nums[idx] in track:
                continue
            # 先进入
            track.append(self.nums[idx])
            self.dfs(track)
            # 再推出
            track.remove(self.nums[idx])


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1, 2, 3]))
