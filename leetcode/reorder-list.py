# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        if not head: 
            return
        if not head.next:
            return head

        #find middle of list
        slowPointer = head
        fastPointer = head

        while fastPointer and fastPointer.next: 
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next


        #reverse list
        second = slowPointer.next
        slowPointer.next = None
        curr = second
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        list2 = prev
        list1 = head
        headList = list1

        #merge list
        while list1 and list2:
            temp1 = list1.next
            temp2 = list2.next

            list1.next = list2
            list2.next = temp1

            list1 = temp1
            list2 = temp2 

        return headList