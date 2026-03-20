class TimeMap(object):

    def __init__(self):
        self.keyList = defaultdict(list)

    def set(self, key, value, timestamp):
        self.keyList[key].append((timestamp, value))
        

    def get(self, key, timestamp):

        if key not in self.keyList:
            return ""
        
        left = 0 
        right = len(self.keyList[key]) - 1
        while left <= right: 
            middle = (left + right) // 2
            if self.keyList[key][middle][0] == timestamp:
                return self.keyList[key][middle][1]
            elif self.keyList[key][middle][0] < timestamp:
                left = middle + 1
            else:
                right = middle - 1

        if right >= 0:
            return self.keyList[key][right][1]
            
        return ""        
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)