class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        '''
        状态是:目前剩的鸡蛋个数K和需要测试的楼层N
        选择:要不要从这层扔鸡蛋
        dp[k][N]:意味着在此状态下的扔鸡蛋次数
        '''
        memo = {}
        def dp(K, N):
            if K == 1:
                return N
            if N == 0:
                return 0
            if (K, N) in memo.keys():
                return memo[(K, N)]
            else:
                res = float("inf")
                for i in range(1, N + 1):
                    res = min(res,
                              max(dp(K, N-i), dp(K-1, i-1)) + 1) # 最坏情况下扔鸡蛋的次数
                memo[(K, N)] = res
                return res

        return dp(K, N)

s = Solution()
s.superEggDrop(K = 3, N = 14)