from typing import List

class Solution:
    def __init__(self):
        self.res = None

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        self.res = [0] + [float("inf") for _ in range(amount)]
        for num in range(1, amount+1):
            for c in coins:
                if num - c >= 0 and self.res[num-c] != float("inf"):
                    self.res[num] = min(self.res[num], self.res[num-c]+1)
        return self.res[-1] if self.res[-1] != float("inf") else -1


if __name__ == "__main__":
    s = Solution()
    res = s.coinChange([2], 3)
    print(res)


