class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0

        length = len(prices)
        for i in range(1, length):
            if buy > prices[i]:
                buy = prices[i]
            profit = max(profit, prices[i] - buy)

        return profit
        