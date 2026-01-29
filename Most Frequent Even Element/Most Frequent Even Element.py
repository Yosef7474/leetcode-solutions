class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        from collections import defaultdict
        
        freq = defaultdict(int)
        
        for num in nums:
            if num % 2 == 0:
                freq[num] += 1
        
        if not freq:
            return -1
        max_freq = max(freq.values())
        
        candidates = [num for num, count in freq.items() if count == max_freq]
        
        return min(candidates)