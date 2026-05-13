class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        left = 0 
        right = 0
        while right < len(prices): 
            maxProfit = max(maxProfit, prices[right] - prices[left])
            while prices[right] - prices[left] < 0: 
                left = right
            right += 1

        return maxProfit