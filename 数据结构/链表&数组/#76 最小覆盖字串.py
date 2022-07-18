
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # record
        need = {}
        for str in t:
            need[str] = need.get(str, 0) + 1
        # 定义valid_len window
        window, valid_len = {}, 0
        best_len, res = len(s) + 1, ""
        l, r = 0, 0
        while r < len(s):
            tmp_char = s[r]
            r += 1
            # 检查当前字符,若为有效字符则更新window
            if tmp_char in need.keys():
                window[tmp_char] = window.get(tmp_char, 0) + 1
                if window[tmp_char] == need[tmp_char]:
                    valid_len += 1
            # 检查当前是否满足收缩条件
            while valid_len == len(need):
                # 更新最优状态
                if r-l < best_len:
                    best_len = r-l
                    res = s[l:r]
                # 窗口剔除left对应字符
                if s[l] in need.keys():
                    if window[s[l]] == need[s[l]]:
                        valid_len -= 1
                    window[s[l]] -= 1
                l += 1
        return res

if __name__ == "__main__":
    s, t = "cjdiuchsics", "cdhc"
    solution = Solution()
    print(solution.minWindow(s, t))