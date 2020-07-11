# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.res = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        '''
        # 初看应该是是二叉树最大路径和的简单版
        ## 做完之后，内心OS：简单题是真简单呀
        '''
        self.DFS(root)
        return self.res - 1 if self.res else 0

    def DFS(self, root):
        if not root:
            return 0
        # 更新一下res
        left = self.DFS(root.left)
        right = self.DFS(root.right)
        self.res = max(self.res, 1 + left + right)
        return 1 + max(left, right)


