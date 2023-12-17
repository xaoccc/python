# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        nodes = []
        new_listnode = ListNode()
        previous = False

        # while head.next:

        #     if head.val != 0:
        #         if previous == True:
        #             result[-1] += head.val
        #         else:
        #             result.append(head.val)

        #         if head.next.val != 0:
        #             result[-1] += head.next.val
        #             head = head.next.next

        #         else:
        #             head = head.next
        #         previous = True

        #     else:
        #         previous = False
        #         head = head.next

        while head.next:
            if head.val != 0:
                if previous:
                    new_listnode.next = head
                else:
                    new_listnode.val = head.val

                if head.next.val != 0:
                    new_listnode.val += head.next.val
                    head = head.next.next

                else:
                    head = head.next
                previous = True
                new_listnode.next = ListNode()

            else:

                previous = False
                head = head.next

        return new_listnode