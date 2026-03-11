class Solution(object):
    def carFleet(self, target, position, speed):
        time = []
        for x in range(len(position)):
            time.append((position[x], float(target - position[x])/speed[x]))
        
        newList = sorted(time, key=lambda item: item[0], reverse=True)
        fleets = 0
        prevTime = 0
        for x in newList: 
            if prevTime < x[1]: 
                fleets += 1
            prevTime = max(prevTime, x[1])
        
        return fleets