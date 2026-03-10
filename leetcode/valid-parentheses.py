class Solution(object):
    def isValid(self, s):
        stack = []
        for x in s: 
            if len(stack) > 0 and ((x == ')' and stack[-1] == '(') or (x == '}' and stack[-1] == '{') or  (x == ']' and stack[-1] == '[')):
                stack.pop()
            else: 
                stack.append(x)

        return len(stack) == 0