# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node_l1 = l1.val
        node_l2 = l2.val
        num1 = ""
        num2 = ""

        result = ListNode()

        while True:
            num1 += str(node_l1)
            if not l1.next:
                break
            node_l1 = l1.next.val
            l1.next = l1.next.next

        while True:
            num2 += str(node_l2)
            if not l2.next:
                break
            node_l2 = l2.next.val
            l2.next = l2.next.next
        num1 = num1[::-1]
        num2 = num2[::-1]

        string_res = str(int(num1) + int(num2))[::-1]

        def create_linked_list(values):
            if not values:
                return None
            head = ListNode(values[0])
            current = head
            for value in values[1:]:
                current.next = ListNode(value)
                current = current.next
            return head

        return create_linked_list(string_res)