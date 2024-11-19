class Solution:
    def hasCycle(self, head) -> bool:
        slow_node = head
        fast_node = head
        if head:
            while fast_node.next:
                slow_node = slow_node.next
                if not fast_node.next.next:
                    break
                fast_node = fast_node.next.next
                if slow_node == fast_node:
                    return True
            return False
        return False
