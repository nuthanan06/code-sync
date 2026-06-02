class Solution(object):
    def groupAnagrams(self, strs):
        newDict = {}
        for x in strs:
            if ''.join(sorted(x)) in newDict: 
                newDict[''.join(sorted(x))].append(x)
            else:
                newDict[''.join(sorted(x))] = [x]

        return list(newDict.values())