class Solution(object):
    def trap(self, height):
        leftMax = 0
        rightMax = 0 
        left = 0
        right = len(height) - 1
        rainWater = 0

        while (left <= right): 
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left]) 
                rainWater += leftMax - height[left]
                left += 1
            else: 
                rightMax = max(rightMax, height[right])
                rainWater += rightMax - height[right]
                right -= 1
        
        return rainWater