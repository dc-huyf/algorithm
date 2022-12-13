'''
# DFS无敌慢
import copy
class Solution:
    def __init__(self):
        self.result = [{}]
    def subsets(self, nums):
        track = set()
        self.DFS(track, nums)
        return [list(k) for k in self.result]

    def DFS(self, track, nums):
        print(self.result)
        if track not in self.result:
            self.result.append(track)
        # 停止条件
        if len(nums) < 1:
            return
        for i in nums:
            if {i} not in self.result:
                self.result.append({i})
            t = copy.deepcopy(track)
            t.add(i)
            tmp = copy.deepcopy(nums)
            tmp.remove(i)
            self.DFS(t, tmp)
'''

# 参考leetcode优秀解答
class Solution:
    def subsets(self, nums):
        result = [[]]
        for i in nums:
            lens = len(result)
            for j in range(lens):
                c = result[j].copy()
                c.append(i)
                result.append(c)
        return result
s = Solution()
s.subsets([1,2,3,4,5])