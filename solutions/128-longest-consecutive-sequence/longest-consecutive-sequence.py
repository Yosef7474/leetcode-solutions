class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        num_set = set(nums)
        longest = 0
        
        for num in nums:
            # Only process if we haven't seen this number in a sequence
            if num in num_set:
                num_set.remove(num)
                left = num - 1
                right = num + 1
                
                # Expand left
                while left in num_set:
                    num_set.remove(left)
                    left -= 1
                
                # Expand right  
                while right in num_set:
                    num_set.remove(right)
                    right += 1
                
                longest = max(longest, right - left - 1)
        
        return longest