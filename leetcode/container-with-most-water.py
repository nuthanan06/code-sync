class Solution(object):
    def maxArea(self, height):
        left = 0 
        right = len(height) - 1
        maxArea = 0

        while (left < right): 
            maxArea = max(maxArea, ((right-left)*min(height[left], height[right])))
            if height[left] <= height[right]: 
                left += 1
            elif height[left] >= height[right]: 
                right -= 1
        
        return maxArea