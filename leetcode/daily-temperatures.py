class Solution(object):
    def dailyTemperatures(self, temperatures):
        indexes = []
        newTemp = [0] * len(temperatures)
        for index, x in enumerate(temperatures):
            while indexes and temperatures[indexes[-1]] < x:
                curr = indexes.pop()
                newTemp[curr] = index - curr

            indexes.append(index)
        
        return newTemp