class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        diff_positions = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_positions.append(i)
        
        if len(diff_positions) != 2:
            return False
        
        i, j = diff_positions
        return s1[i] == s2[j] and s1[j] == s2[i]