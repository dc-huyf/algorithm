from typing import List


class Solution:
    def __init__(self):
        self.nums = None
        self.target = None
        self.memo = {}

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        self.nums = sorted(nums, reverse=True) # 降序排列
        self.target = sum(nums) / k
        if k == 1:
            return True
        if self.target % 1 > 0:
            return False
        used = 0
        return self.dfs(used, k, 0, 0)

    def dfs(self, used, k, sums, idx):
        """
        :param used: 当前已使用数字
        :param k: 当前为第几个桶（剩几个桶）
        :param sums: 当前桶里数字和
        :param idx: 当前数组遍历位置
        :return:
        """
        if k == 0: # 当前是最后一个桶，其他全部已达标，则自然成功
            return True
        if sums == self.target: # 当前桶已经装满,则开始下一个桶，并且数组需从头遍历
            res = self.dfs(used, k-1, 0, 0)
            if res:
                self.memo[used] = res # 记录当前进展详情
                return res

        if used in self.memo.keys(): return self.memo[used]

        for i in range(idx, len(self.nums)):
            if ((used >> i) & 1) == 1 or sums + self.nums[i] > self.target:
                continue
            used |= 1 << i
            if self.dfs(used, k, sums+self.nums[i], i+1): return True
            used ^= 1 << i

        return False


if __name__ == "__main__":
    nums = [2,9,4,7,3,2,10,5,3,6,6,2,7,5,2,4]
    k = 7
    s = Solution()
    res = s.canPartitionKSubsets(nums, k)
    print(res)