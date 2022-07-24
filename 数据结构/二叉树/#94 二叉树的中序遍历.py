# Definition for a binary tree node.
'''
# 我再说最后一遍！！！！球球我自己，记住吧行嘛
# 中序遍历：左根右
# 前序遍历：根左右
# 后序遍历：左右根
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.result = []
    def inorderTraversal(self, root: TreeNode):
        self.main(root)
        return self.result
    def main(self, root):
        if not root:
            return self.result
        if root.left:
            self.main(root.left)
        self.result.append(root.val)
        if root.right:
            self.main(root.right)