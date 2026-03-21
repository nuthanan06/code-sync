from collections import defaultdict

class Solution(object):
    def characterReplacement(self, s, k):
        characterCount = defaultdict(int)
        left = 0
        maxFreq = 0
        maxLength = 0
        
        for right in range(len(s)):
            characterCount[s[right]] += 1
            maxFreq = max(maxFreq, characterCount[s[right]])
            
            if (right - left + 1) - maxFreq > k:
                characterCount[s[left]] -= 1
                left += 1
            
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength