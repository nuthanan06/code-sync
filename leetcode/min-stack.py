class MinStack(object):

    def __init__(self):
        self.array = []

    def push(self, val):
        if (len(self.array) > 0): 
            self.array.append((val, min(self.array[-1][1],val)))
        else: 
            self.array.append((val, val))
        

    def pop(self):
        val = self.array.pop()
        return val[0]        

    def top(self):
        return self.array[-1][0]        

    def getMin(self):
        return self.array[-1][1]        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()