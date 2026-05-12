class Solution(object):
    def productExceptSelf(self, nums):
        
        leftMult = 1
        newList = [1] * len(nums)
        for x in range(len(nums)):
            newList[x] = leftMult
            leftMult *= nums[x]
    
        rightMult = 1
        for x in range(len(nums)):
            newList[len(nums) - x - 1] *= rightMult
            rightMult *= nums[len(nums) - x - 1]
        
        return newList