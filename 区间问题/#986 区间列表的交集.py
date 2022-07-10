class Solution:
    def intervalIntersection(self, A, B):
        if not A or not B:
            return []
        l, r = 0, 0
        res = []
        while l < len(A) and r < len(B):
            inter = self.get_inter(A[l], B[r]) # 两个区间有交集
            if inter:
                res.append(inter)
            if B[r][-1] >= A[l][-1]:
                l += 1
            else:
                r += 1
        return res

    def get_inter(self, l1, l2):
        left = max(l1[0], l2[0])
        right = min(l1[-1], l2[-1])
        if left > right:
            return False
        else:
            return [left, right]

s = Solution()
s.intervalIntersection([[5,10]], [[5,6]])




