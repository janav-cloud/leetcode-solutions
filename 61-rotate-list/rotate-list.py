class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        
        count = 1
        tail = head
        while tail.next:
            tail = tail.next
            count += 1

        
        k = k % count
        if k == 0:
            return head

        
        new_tail = head
        for _ in range(count - k - 1):
            new_tail = new_tail.next

        
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head  

        return new_head