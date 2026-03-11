class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        maxArea = 0
        for index, x in enumerate(heights):
            start = index
            while stack and stack[-1][1] > x:
                pair = stack.pop()
                maxArea = max(maxArea, (index - pair[0]) * pair[1])
                start = pair[0]
        
        
            stack.append((start, x))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea