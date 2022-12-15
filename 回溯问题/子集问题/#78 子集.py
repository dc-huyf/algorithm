from typing import List


class SolutionDFS:
    def __init__(self):
        self.res = []
        self.nums = None

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.dfs([], 0)
        return self.res

    def dfs(self, track, start):
        self.res.append(track)
        for idx in range(start, len(self.nums)):
            track.append(self.nums[idx])
            self.dfs(track[:], idx + 1)
            track.pop()


class SolutionDP:
    """可以转化为递归解法：
    前m个位置的所有非空集合=前m-1位置的集合 + 前m-1位置的集合均加上元素m
    """

    def subsets(self, nums):
        result = [[]]
        for num in nums:
            length = len(result)
            for idx in range(length):
                curr = result[idx].copy()
                curr.append(num)
                result.append(curr)
        return result


if __name__ == "__main__":
    s = SolutionDP()
    res = s.subsets([1, 2, 3, 4, 5])
    print(res)
