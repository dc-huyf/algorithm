# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#     def __init__(self):
#         self.res = 0
#     def diameterOfBinaryTree(self, root: TreeNode) -> int:
#         '''
#         # 初看应该是是二叉树最大路径和的简单版
#         ## 做完之后，内心OS：简单题是真简单呀
#         '''
#         self.DFS(root)
#         return self.res - 1 if self.res else 0
#
#     def DFS(self, root):
#         if not root:
#             return 0
#         # 更新一下res
#         left = self.DFS(root.left)
#         right = self.DFS(root.right)
#         self.res = max(self.res, 1 + left + right)
#         return 1 + max(left, right)

# Definition for a binary tree node.

'''后序遍历'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root: [TreeNode]) -> int:
        self.maxDepth(root)
        return self.res

    def maxDepth(self, root):
        if root is None:
            return 0
        left_len = self.maxDepth(root.left)
        right_len = self.maxDepth(root.right)
        # 更新最大直径
        self.res = max(self.res, left_len + right_len)
        return 1 + max(left_len, right_len)


class Solution2:
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root):
        self.findDepth(root)
        return self.res

    # 求自本节点向下的最大高度
    def findDepth(self, node):
        if node is None:
            return 0
        left_height = self.findDepth(node.left)
        right_height = self.findDepth(node.right)

        # 趁机更新一下最终目标
        self.res = max(self.res, left_height + right_height)

        return 1 + max(left_height, right_height)
