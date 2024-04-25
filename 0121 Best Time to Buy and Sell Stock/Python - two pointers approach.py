# two pointers approach
# time complexity: O(n)

class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        buyingDay, sellingDay = 0, 1
        while sellingDay < len(prices):
            if prices[sellingDay] > prices[buyingDay]:
                maxProfit = max(maxProfit, prices[sellingDay] - prices[buyingDay])
            else:
                buyingDay = sellingDay
            sellingDay += 1
        return maxProfit