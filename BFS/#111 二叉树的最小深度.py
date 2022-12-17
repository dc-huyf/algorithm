from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionDP:
    def minDepth(self, root: TreeNode) -> int:
        # 特殊情况
        if not root: return 0
        children = [root.left, root.right]
        # 停止条件
        if not any(children): return 1
        minDepth = float("inf")
        for r in children:
            if r: minDepth = min(self.minDepth(r), minDepth)
        return minDepth + 1


class SolutionBFS:
    def __init__(self):
        self.res = 0

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue_list = [root]
        self.res += 1
        while len(queue_list) > 0:
            lens = len(queue_list)
            # 逐层遍历
            for i in range(lens):
                cur_root = queue_list.pop(0)
                left = cur_root.left
                right = cur_root.right
                if not left and not right:
                    return self.res
                if left: queue_list.append(left)
                if right: queue_list.append(right)
            # 遍历完一层，深度+1
            self.res += 1
        return self.res




