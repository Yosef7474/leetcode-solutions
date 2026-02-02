# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev_val = None
        min_diff = float('inf')
        
        def inorder(node):
            nonlocal prev_val, min_diff
            
            if not node:
                return
            
            # Traverse left subtree
            inorder(node.left)
            
            # Process current node
            if prev_val is not None:
                min_diff = min(min_diff, abs(node.val - prev_val))
            
            prev_val = node.val
            
            # Traverse right subtree
            inorder(node.right)
        
        inorder(root)
        return min_diff