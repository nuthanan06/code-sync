class Solution(object):
    def generateParenthesis(self, n):
        currList = []
        def recur(numberOpen, numberClose, currString): 
            if numberOpen < n:
                newString = currString + "("
                recur(numberOpen + 1, numberClose, newString)
            if numberClose < n and numberOpen > numberClose:
                newString = currString + ")"  
                recur(numberOpen, numberClose + 1, newString)
            if (len(currString) == (2 * n)): 
                currList.append(currString)

        
        recur(1, 0, "(")
        return currList