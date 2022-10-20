class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        Sell = prices[0]
        MaxProfit = 0
        for price in prices:
            Sell = min(Sell,price)
            Profit = price - Sell
            MaxProfit = max(MaxProfit,Profit)
        return MaxProfit