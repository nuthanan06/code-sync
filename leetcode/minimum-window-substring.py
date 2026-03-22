class Solution(object):
    def minWindow(self, s, t):
        left = 0
        right = 0
        maxLeft = 0
        maxRight = float('inf')

        mainDict = {}
        for x in t:
            mainDict[x] = mainDict.get(x, 0) + 1

        missing = len(t)

        while right < len(s):
            if s[right] in mainDict:
                if mainDict[s[right]] > 0:
                    missing -= 1
                mainDict[s[right]] -= 1
            right += 1

            # shrink window
            while missing == 0:
                if maxRight - maxLeft > right - left:
                    maxRight = right
                    maxLeft = left

                if s[left] in mainDict:
                    mainDict[s[left]] += 1
                    if mainDict[s[left]] > 0:
                        missing += 1
                left += 1

        if maxRight == float('inf'):
            return ""

        return s[maxLeft:maxRight]