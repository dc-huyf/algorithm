class Solution:
    def findAnagrams(self, s: str, p: str):
        '''
        输入:
        s: "cbaebabacd" p: "abc"
        输出:
        [0, 6]
        '''
        left, right = 0, 0
        result = []
        window = {}
        length = float("inf")
        need = {k: p.count(k) for k in p}
        valid = 0
        while right < len(s):
            c = s[right]
            if c in p:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need.keys()): # 达到触发“收缩”的条件
                if right - left + 1 <= length:
                    length = right - left + 1
                    if length == len(p): # 若当下长度满足要求
                        result.append(left)

                d = s[left]
                if need.get(d, 0):
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                left += 1

            right += 1
        return result

s = Solution()
s.findAnagrams(s = "cbaebabacd", p = "abc")

