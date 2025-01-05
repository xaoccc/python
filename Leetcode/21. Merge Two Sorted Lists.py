from typing import Optional


class ListNode:
    def __init__(self):
        self.val = 0
        self.next = None


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = tail = ListNode()
        # If one of the lists does not exist, merging would be adding it to the existing merged list:
        while list1 and list2:
            # Always attach the list with smaller starting value to cur
            # Then move the pointer of this list to the next node
            if list1.val < list2.val:
                tail.next = list1
                list1, tail = list1.next, list1
            else:
                tail.next = list2
                list2, tail = list2.next, list2
        if list1 or list2:
            tail.next = list1 if list1 else list2
        return head.next
