class Solution:
    def getProfit(self, i, isBuying, dp, size, prices):
        if i >= size:
            return 0

        if dp[i][isBuying] != -1:
            return dp[i][isBuying]

        if isBuying:
            buy = self.getProfit(i + 1, 0, dp, size, prices) - prices[i]
            coolDown = self.getProfit(i + 1, 1, dp, size, prices)
            dp[i][isBuying] = max(buy, coolDown)
        else:
            sell = self.getProfit(i + 2, 1, dp, size, prices) + prices[i]
            coolDown = self.getProfit(i + 1, 0, dp, size, prices)
            dp[i][isBuying] = max(sell, coolDown)

        return dp[i][isBuying]

    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        dp = [[-1] * 2 for _ in range(size)]
        return self.getProfit(0, 1, dp, size, prices)