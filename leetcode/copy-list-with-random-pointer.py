"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        
        mappings = {}

        curr = head
        while curr:
            mappings[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            mappings[curr].next = mappings.get(curr.next)
            mappings[curr].random = mappings.get(curr.random)
            curr = curr.next
        
        return mappings[head]