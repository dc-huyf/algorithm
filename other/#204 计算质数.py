class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        res = [True] * (n + 1)
        for i in range(2, n + 1):
            if res[i]: # 若为质数，则其倍数均为False
                a = n // i
                while a > 1:
                    res[a * i] = False
                    a -= 1
        return sum(res[2:-1])

s = Solution()
s.countPrimes(10)