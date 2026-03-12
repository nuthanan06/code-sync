class Solution(object):
    def searchMatrix(self, matrix, target):
        left = 0
        right = len(matrix) - 1
        newMatrix = []
        while left < right: 
            middle = (left + right)//2
            if (matrix[middle][0] == target):
                return True
            elif(matrix[middle][0] <= target and target <= matrix[middle][-1]):
                newMatrix = matrix[middle]
                break
            elif (matrix[middle][0] < target):
                left = middle + 1
            else: 
                right = middle - 1

        if len(newMatrix) == 0: 
            newMatrix = matrix[left]
        
        left = 0 
        right = len(newMatrix) - 1
        while left <= right: 
            middle = (left + right)//2
            if (newMatrix[middle] == target):
                return True
            elif (newMatrix[middle] < target):
                left = middle + 1
            else: 
                right = middle - 1

        return False