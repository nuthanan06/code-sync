class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 1:
            return 0 
        left = 0
        right = 1
        maxProfit = 0
        while right < len(prices): 
            if prices[right] - prices[left] < 0: 
                left += 1
            else: 
                maxProfit = max(maxProfit, (prices[right] - prices[left]))
                right += 1
        
        return maxProfit