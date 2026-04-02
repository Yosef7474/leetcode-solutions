from math import gcd
from collections import defaultdict

class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        g = gcd(n, k)
        operations = 0
        
        for i in range(g):
            values = []
            j = i
            while j < n:
                values.append(arr[j])
                j += g
            
            values.sort()
            median = values[len(values) // 2]
            
            for val in values:
                operations += abs(val - median)
        
        return operations