class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        难点在于：子序列不一定是连续的
        dp[i][j] : 代表s[i:j+1]中删去某些元素后，可以有的最大回文串
        return: dp[0][-1]
        '''
        if len(s) <= 1:
            return len(s)
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i, -1, -1):
                if i == j:
                    dp[j][i] = 1
                else:
                    if s[i] == s[j]:
                        dp[j][i] = dp[j+1][i-1] + 2
                    else:
                        dp[j][i] = max(dp[j+1][i], dp[j][i-1])
        return dp[0][-1]

s = Solution()
s.longestPalindromeSubseq("cbbd")


