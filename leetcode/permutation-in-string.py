class Solution(object):
    def checkInclusion(self, s1, s2):
        s1Dict = defaultdict(int)
        s2Dict = defaultdict(int)
        for x in s1:
            s1Dict[x] += 1
        
        left = 0
        right = 0

        while (right < len(s2)): 
            s2Dict[s2[right]] += 1
            if s2Dict == s1Dict:
                return True
            if s1Dict[s2[right]] == 0: 
                while left <= right: 
                    s2Dict[s2[left]] -= 1
                    left += 1
            if s1Dict[s2[right]] < s2Dict[s2[right]]: 
                while s2[left] != s2[right]: 
                    s2Dict[s2[left]] -= 1
                    left += 1
                s2Dict[s2[left]] -= 1
                left += 1
            right += 1            

        return False