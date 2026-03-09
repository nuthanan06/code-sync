class Solution(object):
    def isPalindrome(self, s):
        s = "".join(x for x in s if x.isalnum())
        s = s.lower()
        leftPointer = 0
        rightPointer = len(s) - 1

        while (leftPointer < rightPointer): 
            if s[leftPointer] != s[rightPointer]: 
                return False
            leftPointer += 1
            rightPointer -= 1

        return True