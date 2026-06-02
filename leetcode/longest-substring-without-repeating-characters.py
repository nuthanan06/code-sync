class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        
        newDict = defaultdict(int)
        maxCounter = 0
        left = 0
        right = 0
        while right < len(s):
            if newDict[s[right]] == 1:
                while s[left] != s[right]: 
                    newDict[s[left]] = 0
                    left += 1
                left += 1
            else:
                newDict[s[right]] = 1
            right += 1
            maxCounter = max(maxCounter, right - left)
        
        return maxCounter