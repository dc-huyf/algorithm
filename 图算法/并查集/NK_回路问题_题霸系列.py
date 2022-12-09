# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

#
# 能回到1号点返回 Yes，否则返回 No
# @param param int整型一维数组 param[0] 为 n，param[1] 为 m
# @param edge Point类一维数组 Point.x , Point.y 分别为一条边的两个点
# @return string字符串
#

class DSU(object):
    def __init__(self, N):
        self.par = list(range(N))
        self.size = [1] * N

    def find(self, p):
        while self.par[p] != p:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def connect(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        pr = self.find(p)
        qr = self.find(q)
        if pr == qr:
            return
        if self.size[pr] > self.size[qr]:
            self.par[qr] = pr
            self.size[pr] += self.size[qr]
        else:
            self.par[pr] = qr
            self.size[qr] += self.size[pr]
        return True


## 方法一：构建除了1之外的连通子图
# class Solution:
#     def solve(self, param, edge):
#         '''
#         首先形成除1外额连通子图，然后查询与1相连的节点中有无在同一个子图中的
#         '''
#         N = param[0]
#         dsu = DSU(N+1)
#         choices = []
#         for p in edge:
#             if p[0] != 1 and p[1] != 1:
#                 dsu.union(p[0], p[1])
#             elif p[0] == 1:
#                 choices.append(p[1])
#             else:
#                 choices.append(p[0])
#
#         # 检查choices内是否有连通点
#         new_c = list(set(choices))
#         for i in range(len(new_c)):
#             for j in range(i+1, len(new_c)):
#                 if dsu.connect(new_c[i], new_c[j]):
#                     return "Yes"
#         return "No"


#
# ## 方法二
# import copy
# class Solution:
#     def solve(self, param, edge):
#         # write code here
#         point_dict = {k: [] for k in range(1, param[0] + 1)}
#
#         for c in edge:
#             point_dict[c[0]].append(c[1])
#             point_dict[c[1]].append(c[0])
#         print(point_dict)
#         # 从1出发
#         return "Yes" if self.DFS(point_dict, 1) else "No"
#
#
#     def DFS(self, point_dict, num):
#         ## 搜索num下的所有选项
#         choices = point_dict[num]
#         if choices == [] and num != 1:
#             return False
#         for i in range(len(choices)):
#             if choices[i] == 1:
#                 return True
#             else:
#                 tmp1 = copy.deepcopy(choices)
#                 choices2 = point_dict[choices[i]]
#                 tmp2 = copy.deepcopy(choices2)
#
#                 tmp1.pop(i)
#                 tmp2.remove(num)
#
#                 point_dict[num] = tmp1
#                 point_dict[choices[i]] = tmp2
#
#                 if self.DFS(point_dict, choices[i]):
#                     return True
#
#                 point_dict[num] = choices
#                 point_dict[choices[i]] = choices2
#
#          return False



s = Solution()
s.solve([4, 4],[(1,2), (2, 3), (3,4),(4,2)])