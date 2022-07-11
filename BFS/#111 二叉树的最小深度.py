class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归方法求解/深度优先搜索
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 特殊情况
        if not root:
            return 0
        children = [root.left, root.right]
        # 停止条件
        if not any(children):
            return 1
        minDepth = float("inf")
        for r in children:
            if r:
                minDepth = min(self.minDepth(r), minDepth)
        return minDepth + 1

# 深度优先搜索，每个节点访问一次，记录到达该节点时的深度
'''
时间复杂度：每个节点恰好被访问一遍，复杂度为 O(N)。
空间复杂度：最坏情况下我们会在栈中保存整棵树，此时空间复杂度为 O(N)。
'''
class Solution1:
    def minDepth(self, root: TreeNode) -> int:
        # 特殊情况
        if not root:
            return 0
        else:
            minDepth = float("inf")
            record = [(1, root)] # 根节点对应的深度

        while record: # 每个节点都能遍历一遍，判为叶子节点就会删除，知道为空
            depth, root = record.pop()
            children = [root.left, root.right]
            if not any(children):
                minDepth = min(depth, minDepth)
            for c in children:
                if c:
                    record.append((depth+1, c))
        return minDepth


# 按照树的层去迭代，第一个访问到的叶子就是最小深度的节点，这样就不用遍历所有的节点了
from collections import deque
# 按照队列存储，先进去的节点先出

class Solution2:
    def minDepth(self, root: TreeNode) -> int:
        # 特殊情况
        if not root:
            return 0
        else:
            minDepth = float("inf")
            record = deque([(1, root)]) # 根节点对应的深度
        while record:
            depth, root = record.popleft()
            children = [root.left, root.right]
            if not any(children): # 一旦到达叶子节点，即可返回
                return depth
            for c in children:
                if c:
                    record.append((depth+1, c))




