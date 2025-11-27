# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            mid = left + (right - left) // 2  # Avoid overflow
            
            if isBadVersion(mid):
                # mid is bad, so first bad version is at mid or before
                right = mid
            else:
                # mid is good, so first bad version is after mid
                left = mid + 1
        
        # left == right, pointing to first bad version
        return left