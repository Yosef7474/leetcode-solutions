# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)  # dummy node to serve as sorted list head
        current = head
        
        while current:
            # Store next node before changing current
            next_node = current.next
            
            # Find insertion position in sorted list
            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            
            # Insert current node
            current.next = prev.next
            prev.next = current
            
            # Move to next node
            current = next_node
        
        return dummy.next