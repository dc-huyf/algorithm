# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode):
        result = []
        cur = deque([root])
        while cur:
            lens = len(cur)
            r = []
            for i in range(lens):
                leaf = cur.popleft()
                if leaf:
                    r.append(leaf.val)
                    if leaf.left:
                        cur.append(leaf.left)
                    if leaf.right:
                        cur.append(leaf.right)
            if r:
                result.append(r)
        return result




