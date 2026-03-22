# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head == None:
            return 
        if head.next == None: 
            return head
        
        currNode = head
        prev = None 

        while currNode != None: 
            temp = currNode.next
            currNode.next = prev
            prev = currNode
            currNode = temp
        
        return prev