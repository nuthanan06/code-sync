class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        prefix = 0
        seen = defaultdict(int)
        seen[0] = 1
        
        for num in nums:
            prefix += num
            count += seen[prefix - k]
            seen[prefix] += 1
        
        return count