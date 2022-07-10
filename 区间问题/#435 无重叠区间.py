class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        '''
        最多互不重叠的区间数量
        '''
        # 按照结束时间排序
        if len(intervals) < 1:
            return 0
        inter = sorted(intervals, key=lambda x: x[1])
        i = 0
        count = 1
        while i <= len(inter):
            target = 0
            for j in range(i+1, len(inter)):
                if inter[j][0] >= inter[i][1]:
                    target = 1
                    count += 1
                    break
            if target == 0:
                return len(intervals) - count
            else:
                i = j
        return len(intervals) - count
s = Solution()
s.eraseOverlapIntervals([[1,2],[1,2], [1,2] ])