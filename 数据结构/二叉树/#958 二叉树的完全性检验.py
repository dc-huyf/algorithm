# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        h = 0
        record = deque([root])
        stop = False
        while record:
            lens = len(record)
            # 注意更新层数
            for _ in range(lens):
                node = record.popleft()
                left = node.left
                right = node.right
                if left:
                    if stop:
                        return False
                    record.append(left)
                else:
                    stop = True
                if right:
                    if stop:
                        return False
                    record.append(right)
                else:
                    stop = True
        return True