class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)

        while left <= right:
            middle = (left + right)//2
            counter = 0
            for x in piles: 
                counter += math.ceil(float(x)/middle)
            if counter > h:
                left = middle + 1
            else:
                right = middle - 1
        
        return left