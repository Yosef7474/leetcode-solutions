class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine sign
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        # Convert to positive
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)
        
        result = 0
        
        # Subtract divisor in exponential steps
        while dividend_abs >= divisor_abs:
            shift = 0
            # Find the largest divisor * 2^shift that fits in dividend
            while dividend_abs >= (divisor_abs << (shift + 1)):
                shift += 1
            
            # Add 2^shift to result
            result += 1 << shift
            # Subtract divisor * 2^shift from dividend
            dividend_abs -= divisor_abs << shift
        
        return sign * result