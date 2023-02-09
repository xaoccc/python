class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        str_head = ''
        while head:            
            str_head += str(head.val)
            head = head.next
        return int(str_head, 2)
