# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            # Identify the two nodes to swap
            first = prev.next
            second = first.next
            
            # Save the node after the pair
            third = second.next
            
            # Perform the swap
            prev.next = second
            second.next = first
            first.next = third
            
            # Move prev forward for the next pair
            prev = first
        
        return dummy.next