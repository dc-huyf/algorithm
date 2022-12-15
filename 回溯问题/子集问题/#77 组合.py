from typing import List


class SolutionDFS:
    def __init__(self):
        self.res = []
        self.nums = None

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.nums = list(range(1, n+1))
        self.dfs(0, [], k)
        return self.res

    def dfs(self, idx, track, K):
        if K == 0:
            self.res.append(track)
            return
        for i in range(idx, len(self.nums)):
            track.append(self.nums[i])
            self.dfs(i+1, track[:], K-1)
            track.pop()


class SolutionDP:
    """
    递归思路：dp(m, k) = dp(m-1, k) + dp(m-1, k-1) & nums[m]
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))
        if k == 0: return [[]]
        if k == n: return [nums]
        mid1 = self.combine(n - 1, k - 1)
        mid2 = self.combine(n - 1, k)
        mid3 = []
        for item in mid1:
            item.append(nums[-1])
            mid3.append(item)
        return mid2 + mid3


if __name__ == "__main__":
    s = SolutionDP()
    res = s.combine(3, 2)
    print(res)
