# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        record = deque([root])
        h = 0
        while record:
            lens = len(record)
            for _ in range(lens):
                cur = record.popleft()
                left = cur.left
                right = cur.right
                if left:
                    record.append(left)
                if right:
                    record.append(right)
            h += 1
        return h