class Solution(object):
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        max_length = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                length = 1
                
                # check if the current length can be beaten and we only look for the minimum one and then add from there, use sets for O(1)
                while num + length in nums_set:
                    length += 1

                max_length = max(max_length, length)

        return max_length