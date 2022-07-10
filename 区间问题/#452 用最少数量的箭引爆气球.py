class Solution:
    def findMinArrowShots(self, points) -> int:
        '''
        [[10,16], [2,8], [1,6], [7,12]]
        '''
        ## 有几个不重叠的区间，就需要射出几箭
        if not points:
            return 0
        count = 1
        i = 0
        points = sorted(points, key=lambda x:x[-1])
        while i <= len(points):
            target = 0
            for j in range(i+1, len(points)):
                if points[j][0] > points[i][-1]: # j与i不重叠
                    target = 1
                    count += 1  # 表示不重叠的数量
                    break
            if target == 0: # i之后并未有与其重叠的区域
                return count
            else:
                i = j
        return count

s = Solution()
s.findMinArrowShots([[10,16], [2,8], [1,6], [7,12]])



