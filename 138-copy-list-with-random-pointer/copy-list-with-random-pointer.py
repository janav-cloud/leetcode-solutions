class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        # Create copies and interweave them
        current = head
        while current:
            # the new node
            new = Node(
                x=current.val
                , next=current.next  # point to the original next
                , random=current.random  # point to the original random
            )
            current.next = new
            current = new.next

        # Update nexts and randoms by pointing their pointers to .next
        # This works because each pointer should now have an adjacent "copy"
        new_head = head.next
        current = new_head
        while current:
            current.next = current.next.next if current.next else None
            current.random = current.random.next if current.random else None
            current = current.next
        return new_head
        