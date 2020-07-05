import numpy as np
class Solution:
    def superPow(self, a: int, b) -> int:
        dp = [a ** i % 1337 for i in range(10)]
        ans = a ** b[-1] % 1337
        for n in b[::-1]:
            for i in range(10):
                dp[i] = dp[i] ** 10 % 1337
            res = ans * dp[n] % 1337
        return ans
s = Solution()
s.superPow(2, [1,4,5,6])

