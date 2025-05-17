# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy

        while True:
            kth = self.getKthNode(groupPrev, k)
            if kth is None:
                break

            groupEnd = kth
            groupStart = groupPrev.next
            nextGroupStart = groupEnd.next

            groupEnd.next = None
            groupPrev.next = self.reverseList(groupStart)
            groupStart.next = nextGroupStart

            groupPrev = groupStart
        return dummy.next

    def getKthNode(self, head, k):
        for i in range(k):
            if head.next is not None:
                head = head.next
            else:
                return None
        return head

    def reverseList(self, head):
        prev = None
        while head:
            current = head
            forward = head.next
            head.next = prev
            prev = current
            head = forward
        return prev