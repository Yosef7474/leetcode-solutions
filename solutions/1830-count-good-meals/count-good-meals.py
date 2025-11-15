class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10**9 + 7
        count = 0
        freq = {}
        
        powers = [1 << i for i in range(22)]  # [1, 2, 4, ..., 2^21]
        
        for d in deliciousness:
            for power in powers:
                complement = power - d
                if complement in freq:
                    count = (count + freq[complement]) % MOD
            freq[d] = freq.get(d, 0) + 1
        
        return count