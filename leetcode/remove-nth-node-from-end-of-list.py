# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        counter = 0        
        
        #find length of array
        curr = head
        counter = 0
        while curr:
            counter += 1
            curr = curr.next
        #remove 
        newN = counter - n
        if newN == 0: 
            return head.next
        
        counter = 0 
        prev = None
        curr = head
        while curr and counter < newN: 
            prev = curr
            curr = curr.next
            counter += 1
        
        prev.next = curr.next
        curr.next = None
        return head