class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from queue import PriorityQueue
        q = PriorityQueue()
        N = len(lists)
        reshead = ListNode(-1)
        p = reshead
        for i in range(N):
            if lists[i]:
                q.put((lists[i].val,i,lists[i]))
        while q.qsize():
            val, i , node = q.get()
            if node.next:
                q.put((node.next.val,i,node.next))
            p.next = node
            p = p.next      
        return reshead.next
    