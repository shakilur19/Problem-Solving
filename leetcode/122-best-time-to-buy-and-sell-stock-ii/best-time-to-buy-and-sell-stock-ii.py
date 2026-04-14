class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        ai = prices[0]
        aj = 0

        for i in range(1, size):
            aj = max(aj, aj + (prices[i] - ai))
            ai = prices[i]

        return aj