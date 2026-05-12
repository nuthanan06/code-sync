class Solution(object):
    def threeSum(self, nums):
        noDupes = []
        nums = sorted(nums) # O(log n)

        for x in range(len(nums)):
            if nums[x] > 0:
                break

            if x > 0 and nums[x] == nums[x - 1]:
                continue

            left = x + 1
            right = len(nums) - 1
            while left < right: 
                if nums[left] + nums[right] + nums[x] == 0:
                    noDupes.append((nums[x], nums[left], nums[right]))
                    right -= 1
                    left += 1
                    while nums[right] == nums[right + 1] and left < right: 
                        right -= 1
                    while nums[left] == nums[left - 1] and left < right:  
                        left += 1
                elif nums[left] + nums[right] + nums[x] > 0: 
                    right -= 1
                else:
                    left += 1
            
        return noDupes