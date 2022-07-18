class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window, max_len = {}, 0
        l, r = 0, 0
        while r < len(s):
            tmp_char = s[r]
            r += 1
            window[tmp_char] = window.get(tmp_char, 0) + 1
            while window[tmp_char] > 1:
                char = s[l]
                l += 1
                window[char] -= 1
            max_len = max(max_len, r - l)

        return max_len


if __name__ == "__main__":
    s = "abcabcbb"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))
