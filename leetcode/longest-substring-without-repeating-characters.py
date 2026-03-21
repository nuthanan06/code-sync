class Solution(object):
    def lengthOfLongestSubstring(self, s):
        characterDict = defaultdict(int)
        if len(s) == 0: 
            return 0
        elif len(s) == 1: 
            return 1
        
        left = 0
        right = 0
        maxCount = 0
        while (right < len(s)):
            if characterDict[s[right]] == 0: 
                characterDict[s[right]] = 1
                right += 1
                maxCount = max(maxCount, right - left)
            else: 
                while s[left] != s[right]: 
                    characterDict[s[left]] -= 1
                    left += 1
                right += 1
                left += 1
                    
        return maxCount