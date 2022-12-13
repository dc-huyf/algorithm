import copy
class Solution:
    def __init__(self):
        self.result = [[]]
    def combine(self, n: int, k: int):
        track = []
        self.DFS(track, n, k)
        if len(self.result) > 1:
            self.result.remove([])
        return self.result

    def DFS(self, track, n, k):
        # 停止条件
        if len(track) == k:
            if track not in self.result:
                self.result.append(track)
        if n == 0:
            return
        for i in range(n, 0, -1):
            # 可以选择加i
            tmp1 = copy.deepcopy(track)
            tmp1.extend([i])
            self.DFS(tmp1, i-1, k)

s = Solution()
s.combine(14, 2)



