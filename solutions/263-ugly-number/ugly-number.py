class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        # Divide by 2, 3, 5 as much as possible
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        
        # If n becomes 1, it only has prime factors 2, 3, 5
        return n == 1