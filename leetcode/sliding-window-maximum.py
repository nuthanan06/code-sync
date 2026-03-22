class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if k == 1:
            return nums
        outputList = [x for x in range(len(nums) - k + 1)]
        queue = deque()
        left = 0 
        right = 0
        while right < len(nums): 
            #dealing with right pointer
            while len(queue) != 0 and nums[queue[-1]] < nums[right]: 
                queue.pop()
            queue.append(right)

            #append max and shift left
            if right - left == k - 1:
                outputList[right - k + 1] = nums[queue[0]]
                while queue[0] <= left:
                    queue.popleft()
                left += 1
            
            right += 1
        
        return outputList