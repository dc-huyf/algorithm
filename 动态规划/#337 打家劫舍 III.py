# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.tree = {}

    def rob(self, root: TreeNode) -> int:
        '''
        对于当前节点：无非是偷/不偷；
        偷的话，可以再去偷下下家
        不偷，则收益为下家
        ## 设置备忘录：1. 减少计算；2.防止自底向上过程中，值发生变化
        '''
        return self.DFS(root)

    def DFS(self, root):
        if not root:
            return 0
        if root in self.tree.keys():
            return self.tree[root]
        left = root.left
        right = root.right
        l_l = self.DFS(left.left) if left != None else 0
        l_r = self.DFS(left.right) if left != None else 0
        r_l = self.DFS(right.left) if right != None else 0
        r_r = self.DFS(right.right) if right != None else 0

        root.val = max(root.val + l_l + l_r + r_l + r_r,
                       self.DFS(left) + self.DFS(right))
        self.tree[root] = root.val
        return root.val