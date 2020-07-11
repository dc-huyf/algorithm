class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution1:
    def preorderTraversal(self, root: TreeNode):
        res = []
        self.DFS(root, res)
        return res

    def DFS(self, root, res):
        if not root:
            return
        # 加入根节点的值
        res.append(root.val)
        self.DFS(root.left, res)
        self.DFS(root.right, res)


# 利用栈，后进后出
class Solution2:
    def preorderTraversal(self, root: TreeNode):
        if not root:
            return []
        record = [root]
        res = []
        while record:
            cur = record.pop()
            res.append(cur.val)
            left = cur.left
            right = cur.right
            if right:
                record.append(right)
            if left:
                record.append(left)
        return res




