```buildoutcfg
# 全排列问题代码参考
# 路径：记录在 track 中
# 选择列表：nums 中不存在于 track 的那些元素
# 结束条件：nums 中的元素全都在 track 中出现

class Solution:
    def __init__(self):
        self.res = []
    def permute(self, nums):
        track = []
        self.backtrack(nums, track)
        return self.res
    def backtrack(self, nums, track):
        # 触发结束条件
        if len(track) == len(nums):
            self.res.append(track)
            return
        
        # 遍历每个选择
        for i in range(len(nums)):
            # 排除不合法选择
            if nums[i] in track:
                continue;
            # 做选择
            tmp = copy.deepcopy(track)
            tmp += [nums[i]]
            # 进入下一层决策树
            self.backtrack(nums, tmp)
            # 取消选择,以便进行下一个选择
            # track.pop()
```