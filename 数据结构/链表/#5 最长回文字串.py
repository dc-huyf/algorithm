'''
本题也可用【动态规划】做法
此处只写双指针做法
'''
class Solution:
    def getMaxLenString(self, ss, l, r):
        res = ""
        while l>=0 and r<len(ss) and ss[l] == ss[r]:
            res = ss[l: r+1]
            l -= 1
            r += 1
        return res

    def longestPalindrome(self, s: str) -> str:
        res = ""
        if len(s) < 2:
            return s
        for i in range(len(s)):
            s1 = self.getMaxLenString(s, i, i)
            s2 = self.getMaxLenString(s, i, i+1)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome('aaabaaaabaa'))