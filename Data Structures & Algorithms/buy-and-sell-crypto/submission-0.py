class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for i in prices:
            if i < buy:
                buy = i
            curr_profit = i - buy

            profit = max(profit, curr_profit)
        return profit
