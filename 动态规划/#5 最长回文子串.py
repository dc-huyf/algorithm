def longestPalindrome(s):
    '''
    功能简化：
    判断是否回文是简单的
    dp[i][j]: 记录s[i:j+1]是否为回文串 True/False
    max_len: 记录目前最大长度
    start: 记录开始位置指针
    '''
    if len(s) <= 1:
        return s
    dp = [[False for i in range(len(s))] for _ in range(len(s))]
    max_len = 1
    start = 0
    for i in range(len(s)):
        dp[i][i] = True
        for j in range(i-1, -1, -1):
            if s[j] == s[i]:
                if i - j <= 2:
                    dp[j][i] = True
                    if i - j + 1 > max_len:
                        start, max_len = j, i - j + 1
                else:
                    if dp[j+1][i-1] == True:
                        dp[j][i] = True
                        if i - j + 1 > max_len:
                            start, max_len = j, i - j + 1
    return s[start: start + max_len]

longestPalindrome('aaaaa')