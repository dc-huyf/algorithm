class Solution:
    def merge(self, intervals):
        '''
        输入: [[1,3],[2,6],[8,10],[15,18]]
        输出: [[1,6],[8,10],[15,18]]
        解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
        '''
        if not intervals:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        result = []
        i = 0
        cur = intervals[0]
        while i < len(intervals)-1:
            target = 0
            for j in range(i+1, len(intervals)):
                target = 1
                if intervals[j][0] > cur[-1]:
                    result.append(cur)
                    cur = intervals[j]
                    i = j
                    break
                else:
                    cur = [min(cur[0], intervals[j][0]), max(cur[-1], intervals[j][-1])]
                    i += 1
        result.append(cur)
        return result

s = Solution()
s.merge([[2,3],[4,5],[6,7],[8,9],[1,10]])

