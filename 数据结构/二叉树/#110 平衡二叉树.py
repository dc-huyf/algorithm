# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root) -> bool:
        '''
        # 平衡二叉树：每个节点左右相差不超过1
        '''
        return self.depth(root) != -1

    # 计算深度+判断平衡
    def depth(self, root):
        '''
        若平衡则返回深度，若非平衡则返回-1
        '''
        # 以下两个特殊情形均为平衡
        if not root:
            return 0
        elif not root.left and not root.right:  # 叶子节点
            return 1
        else:
            left = self.depth(root.left)
            right = self.depth(root.right)
            # 若左右子树非平衡，直接返回
            if left == -1: return -1
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1