# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        newList = None
        carry = 0 
        ref = None
        while l1 and l2: 
            sumVal = l1.val + l2.val + carry
            if sumVal > 9: 
                carry = 1
                sumVal = sumVal - 10
            else:
                carry = 0

            if not newList:
                newList = ListNode(sumVal)
                ref = newList
            else:
                newList.next = ListNode(sumVal)
                newList = newList.next
            l1 = l1.next
            l2 = l2.next
        
        while l1: 
            sumVal = l1.val + carry
            if sumVal > 9: 
                carry = 1
                sumVal = sumVal - 10
            else:
                carry = 0

            if not newList:
                newList = ListNode(sumVal)
                ref = newList
            else:
                newList.next = ListNode(sumVal)
                newList = newList.next
            l1 = l1.next

        while l2: 
            sumVal = l2.val + carry
            if sumVal > 9: 
                carry = 1
                sumVal = sumVal - 10
            else:
                carry = 0

            if not newList:
                newList = ListNode(sumVal)
                ref = newList
            else:
                newList.next = ListNode(sumVal)
                newList = newList.next
            l2 = l2.next

        if carry != 0: 
            newList.next = ListNode(carry)
        return ref