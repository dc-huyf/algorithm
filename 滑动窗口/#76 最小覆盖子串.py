class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        滑动窗口来实现:
        1. right + 1: 扩张
        2. left + 1: 收缩
        3. 使用字典记录当前窗口字符类型和数量，window need
        '''
        # 初始化need
        need = {}
        for ss in t:
            need[ss] = need.get(ss, 0) + 1
        window = {}
        left, right = 0, 0
        valid = 0

        # 初始化结果参数
        start = 0
        length = float("inf")

        while right < len(s):
            c = s[right]
            if c in t: # 若c在t中，非无效字符
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            # 当window满足覆盖条件时，则开始收缩
            while valid == len(need.keys()):
                if right - left + 1 < length:
                    start = left
                    length = right - left + 1

                m = s[left]
                left += 1
                if need.get(m, 0):
                    if window[m] == need[m]:
                        valid -= 1
                    window[m] = window[m] - 1
            right += 1

        if length == float("inf"):
            return ""
        else:
            return s[start: start + length]


s = Solution()
s.minWindow(s = "ADOBECODEBANC", t = "ABC")


