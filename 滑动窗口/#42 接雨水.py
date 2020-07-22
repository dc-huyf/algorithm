class Solution:
    def trap(self, height) -> int:
        '''
        思路蛮重要的
        每个格子的存水量 = min(left_max[i], right_max[i]) - height[i]
        '''
        if len(height) <= 2:
            return 0
        left_max = [height[0]]
        right_max = [height[-1]]
        res = 0
        for i in range(1, len(height)):
            left_max.append(max(left_max[-1], height[i]))
        for j in range(len(height) - 2, -1, -1):
            right_max.append(max(right_max[-1], height[j]))
        right_max = right_max[::-1]
        for h in range(len(height)):
            res += (min(left_max[h], right_max[h]) - height[h])
        return res
s = Solution()
s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
