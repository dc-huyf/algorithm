# 好多牛牛
# @param s string字符串
# @return int整型
#
class Solution:
    def solve(self, s):
        # write code here
        t = 'niuniu'
        dp = [0] * len(t)
        for i in s:
            if i == 'n':
                dp[0] = (dp[0] + 1) % (10 ** 9 + 7)
                dp[3] = (dp[2] + dp[3]) % (10 ** 9 + 7)
            if i == 'i':
                dp[1] = (dp[0] + dp[1]) % (10 ** 9 + 7)
                dp[4] = (dp[4] + dp[3]) % (10 ** 9 + 7)
            if i == 'u':
                dp[2] = (dp[2] + dp[1]) % (10 ** 9 + 7)
                dp[5] = (dp[4] + dp[5]) % (10 ** 9 + 7)
        return dp[-1]

s = Solution()
a = s.solve("vgylwgbusbmborxtlhcsmpxohgmgnkeufdxotogbgxpeyanfetcukepzshkljugggekjdqzjenpevqgxiepjsrdzjazujllchhbfqmkimwzobiwybxduunfsksrsrtekmqdcyzjeeuhmsrqcozijipfioneeddpszrnavymmtatbdzqsoemuvnpppsuacbazuxmhecthlegrpunkdmbppweqtgjoparmowzdqyoxytjbbhawdydcprjbxphoohpkwqyuhrqzhnbnfuvqnqqlrzjpxiogvliexdzuzosrkrus")