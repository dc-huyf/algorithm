class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # record
        need = {}
        for str in s1:
            need[str] = need.get(str, 0) + 1
        # 定义valid_len window
        window, valid_len = {}, 0
        l, r = 0, 0
        while r < len(s2):
            tmp_char = s2[r]
            r += 1
            # 检查当前字符,若为有效字符则更新window
            if tmp_char in need.keys():
                window[tmp_char] = window.get(tmp_char, 0) + 1
                if window[tmp_char] == need[tmp_char]:
                    valid_len += 1
            # 检查当前是否满足收缩条件
            while valid_len == len(need):
                # 更新最优状态
                if r - l == len(s1):
                    return True
                # 窗口剔除left对应字符
                if s2[l] in need.keys():
                    if window[s2[l]] == need[s2[l]]:
                        valid_len -= 1
                    window[s2[l]] -= 1
                l += 1

        return False


if __name__ == "__main__":
    s1, s2 = "ab", "eidbaooo"
    solution = Solution()
    print(solution.checkInclusion(s1, s2))