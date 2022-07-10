class Solution:
    def tallestBillboard(self, rods) -> int:
        dp = {0: 0} # key记录高度差， value记录当前最大正数和
        for i in rods:
            new_dp = dp.copy()
            for j in dp:
                new_dp[j+i] = max(new_dp.get(j+i, 0), dp[j]) # 加到较高的一边
                if j >= i:
                    new_dp[j-i] = max(new_dp.get(j-i,0), dp[j] + i)  # 加到较低的一边后，并未超过另一边
                else:
                    new_dp[i-j] = max(new_dp.get(i-j,0), dp[j] + j)  # 加到较低的一边后，超过另一边
            dp = new_dp
        return dp[0]