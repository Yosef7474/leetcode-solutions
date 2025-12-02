class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        current_end = 0  # Current farthest reachable with current jumps
        farthest = 0     # Farthest we can reach
        
        for i in range(n - 1):  # Don't need to check last element
            # Update the farthest we can reach from current position
            farthest = max(farthest, i + nums[i])
            
            # If we've reached the end of current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # If we can already reach the end
                if current_end >= n - 1:
                    break
        
        return jumps