# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        new_listnode = ListNode()

        while head.next:
            result.append(head.val)
            head = head.next

        for node in result:
            if node == 0:
                continue
            else:
                new_listnode.val = node
                new_listnode.next = ListNode()

        return new_listnode