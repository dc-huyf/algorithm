class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        包含s1的最小字符串如果长度比s1长，则返回False
        '''
        left, right = 0, 0
        need = {}
        for ss in s1:
            need[ss] = need.get(ss, 0) + 1
        window = {}
        valid = 0
        length = float("inf")
        while right < len(s2):
            c = s2[right]
            if need.get(c, 0) > 0: # 为目标字符
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need.keys()): # 出现能够符合条件的了
                length = min(length, right - left + 1)
                d = s2[left]
                if need.get(d, 0): # left位置字符为有效字符
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                left += 1
            right += 1
        if length == len(s1):
            return True
        else:
            return False

s = Solution()
s.checkInclusion(s1 = "adc", s2 = "dcda")


