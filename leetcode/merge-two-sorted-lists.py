class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1

        if list2.val < list1.val:
            list1, list2 = list2, list1

        currHead = list1
        prev = None

        while list1 and list2:
            if list1.val <= list2.val:
                prev = list1
                list1 = list1.next
            else:
                temp = list2.next
                prev.next = list2
                list2.next = list1
                prev = list2
                list2 = temp

        if list2:
            prev.next = list2

        return currHead