class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        def expand_around_center(left, right):
            # Expand outwards while the substring is palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome substring
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            # Check for odd-length palindromes (single character center)
            palindrome_odd = expand_around_center(i, i)
            # Check for even-length palindromes (two character center)
            palindrome_even = expand_around_center(i, i + 1)
            
            # Update longest palindrome found
            if len(palindrome_odd) > len(longest):
                longest = palindrome_odd
            if len(palindrome_even) > len(longest):
                longest = palindrome_even
        
        return longest