# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge case: empty list or single node
        if not head or not head.next:
            return head
        
        # Step 1: Find the k-th node from the beginning
        first = head
        for _ in range(k - 1):
            first = first.next
        
        # Step 2: Find the k-th node from the end
        # Use two pointers: start second from head, but move it only after
        # we've moved another pointer k steps ahead
        second = head
        temp = first
        
        # Move temp to the end, and second will end up at (n-k+1)-th node
        while temp.next:
            second = second.next
            temp = temp.next
        
        # Step 3: Swap the values
        first.val, second.val = second.val, first.val
        
        return head