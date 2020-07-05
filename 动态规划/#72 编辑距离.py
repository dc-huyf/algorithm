# 回溯会严重超时
def minDistance(word1, word2):
    '''
    思路：
    求解编辑距离？？NLP中蛮常见的场景
    三种操作：插入、删除、替换
    形成自己的编辑逻辑
    '''
    if len(word1) == 0 or len(word2) == 0:
        return abs(len(word1) - len(word2))
    else:
        return cal_times(word1, word2)

def cal_times(s1, s2):
    if len(s2) == 0:
        return len(s1)
    if len(s1) == 0:
        return len(s2)
    if s1[0] == s2[0]:
        return cal_times(s1[1:], s2[1:])
    else:
        return 1 + min(cal_times(s1[1:], s2[1:]), cal_times(s1, s2[1:]), cal_times(s1[1:], s2))



# 想办法解决超时问题：使用动态规划
def cal_times_dp(word1, word2):
    '''
    动态规划求解这个问题：
    dp[i][j] :代表word1[:i+1] -> word2[:j+1] 所需要的次数
    若word1[i] == word2[j],则dp[i][j] = dp[i - 1][j - 1]
    若word1[i] == word2[j],则1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        - word1[:i] -> word2[:j]就位后, 再替换最后一位
        - word1[:i] -> word2[:j+1]就位后，删除word1最后一位
        - word1[:i+1] -> word2[:j]就位后，插入word1最后一位
    '''
    len1 = len(word1)
    len2 = len(word2)
    if len1 == 0 or len2 == 0:
        return abs(len1 - len2)
    dp = [[0 for i in range(len1)] for j in range(len2)]
    if word1[0] != word2[0]:
        dp[0][0] = 1
    for i in range(1, len1):
        dp[0][i] = i if dp[0][i-1] < i else (i if word1[i] == word2[0] else i+1)
    for j in range(1, len2):
        dp[j][0] = j if dp[j-1][0] < j else (j if word1[0] == word2[j] else j+1)
    for j in range(1, len1):
        for i in range(1, len2):
            if word1[j] == word2[i]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    return dp[-1][-1]

s1 = "a"
s2 = "ab"

cal_times_dp(s1, s2)