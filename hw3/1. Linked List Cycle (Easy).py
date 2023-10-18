class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow,fast=head,head.next
        while fast!=slow:
            if not fast.next or not fast.next.next:
                return False
            slow=slow.next
            fast=fast.next.next
        return True