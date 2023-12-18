# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nodes = []
        nodes_sum = 0

        while head.next is not None:
            if head.val != 0:
                nodes_sum += head.val

            elif head.val == 0 and nodes_sum != 0:
                nodes.append(nodes_sum)
                nodes_sum = 0

            if head is not None:
                head = head.next
        if nodes_sum != 0:
            nodes.append(nodes_sum)

        result = ListNode()
        tmp = result
        for n in nodes:
            tmp.next = ListNode(n)
            tmp = tmp.next

        return result.next