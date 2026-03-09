class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        array = []
        for k in range(len(nums)): 
            leftPointer = k + 1
            rightPointer = len(nums) - 1
            if nums[k] > 0 or (k > 0 and nums[k] == nums[k - 1]):
                continue 

            while (leftPointer < rightPointer):
                if nums[leftPointer] + nums[rightPointer] + nums[k] == 0: 
                    array.append((nums[leftPointer], nums[rightPointer], nums[k]))
                    
                    leftPointer += 1
                    rightPointer -= 1

                    while leftPointer < rightPointer and nums[leftPointer] == nums[leftPointer - 1]:
                        leftPointer += 1

                    while leftPointer < rightPointer and nums[rightPointer] == nums[rightPointer + 1]:
                        rightPointer -= 1
                        
                elif nums[leftPointer] + nums[rightPointer] + nums[k] < 0: 
                    leftPointer += 1
                else: 
                    rightPointer -= 1
                        
        return array