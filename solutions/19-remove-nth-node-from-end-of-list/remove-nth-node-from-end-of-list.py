# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        fast = slow = dummy

    # move fast n steps ahead
        for _ in range(n):
            fast = fast.next

    # move both until fast reaches end
        while fast.next:
            fast = fast.next
            slow = slow.next

    # remove node
        slow.next = slow.next.next

        return dummy.next

        return head
        