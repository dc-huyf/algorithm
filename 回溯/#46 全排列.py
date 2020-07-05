# class Solution:
#     '''
#     回溯问题：
#     1. self.res记录所有可能的路径
#     2. 传入参数track:记录当前路径（初始路径）
#     3. 设置停止条件
#     4. 遍历每个选择
#     5. 递归调用
#     '''
#
#     def __init__(self):
#         self.res = []
#
#     def permute(self, nums):
#         '''
#         经典的回溯问题：
#         '''
#         self.result(nums, [])
#         return self.res
#
#     def result(self, nums, track):
#         if len(nums) == 0:
#             self.res.append(track)
#         for i in range(len(nums)):
#             tmp = self.result(nums[:i] + nums[i+1:], track + [nums[i]])
#             if tmp is not None:
#                 self.res.append(tmp)
import copy
class Solution:
    def __init__(self):
        self.res = []
    def permute(self, nums):
        self.backtrack(nums, [])
        return self.res

    def backtrack(self, nums, track):
        # 触发结束条件
        if len(track) == len(nums):
            print(track)
            self.res += [track]
            print(self.res)
            return
        # 遍历每个选择
        for i in range(len(nums)):
            # 排除不合法选择
            if nums[i] in track:
                continue
            # 做选择
            tmp = copy.deepcopy(track)
            tmp += [nums[i]]
            # 进入下一层决策树
            self.backtrack(nums, tmp)
            # 取消选择,以便进行下一个选择
            # track.pop()

s = Solution()
print(s.permute([1,2,3]))