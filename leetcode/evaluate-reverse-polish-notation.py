class Solution(object):
    def evalRPN(self, tokens):
        numStack = []
        for x in tokens: 
            if x == '+': 
                num1 = numStack.pop()
                num2 = numStack.pop()
                numStack.append(num1 + num2)
            elif x == '-': 
                num1 = numStack.pop()
                num2 = numStack.pop()
                numStack.append(num2 - num1)
            elif x == '*':
                num1 = numStack.pop()
                num2 = numStack.pop()
                numStack.append(num1 * num2)
            elif x == '/':
                num1 = numStack.pop()
                num2 = numStack.pop()
                numStack.append(int(float(num2)/num1))
            else: 
                numStack.append(int(x))

        return numStack[-1]