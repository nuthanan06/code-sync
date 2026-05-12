class Solution(object):
    def twoSum(self, nums, target):
        hashMap = set(nums)

        for x in range(len(nums)):
            if target - nums[x] in hashMap and x != nums.index(target - nums[x]): 
                return [x, nums.index(target - nums[x])]