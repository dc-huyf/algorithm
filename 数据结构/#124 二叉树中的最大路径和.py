# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = -float("inf")
    def maxPathSum(self, root: TreeNode) -> int:
        self.DFS(root)
        return self.res
    def DFS(self, root):
        if not root:
            return 0
        # 左孩子的贡献
        leftMax = max(0, self.DFS(root.left))
        rightMax = max(0, self.DFS(root.right))
        # 更新一下res
        self.res = max(self.res, root.val + leftMax + rightMax)
        return root.val + max(leftMax, rightMax)