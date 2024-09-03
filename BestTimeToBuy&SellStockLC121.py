
#You are given an array prices where prices[i] is the price of a given stock on the ith day.

#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day
# in the future to sell that stock.

#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
# Solution : start with index 1. let buy date & profit be 0
# if stock available for cheaper update buy price
# if profit of cur index greater than old profit, update profit
# old max profit remembered and updates buy to lower value after market crash
# return max profit
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
print(Solution().maxProfit([2,1,3,1,0,1]))