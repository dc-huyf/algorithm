class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口
        left, right = 0, 0
        length = 0
        window = {}
        # 注意记录每次扩张/缩放步骤的更新，不需要记录最长字串是什么
        while right < len(s):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            while window[c] >= 2: # 一重复就收缩,即便左边不是c,会一直收缩到c的数量为1为止
                d = s[left]
                left += 1
                window[d] -= 1
            length = max(length, right - left + 1)
            right += 1
        return length

s = Solution()
s.lengthOfLongestSubstring("abcabcbb")







