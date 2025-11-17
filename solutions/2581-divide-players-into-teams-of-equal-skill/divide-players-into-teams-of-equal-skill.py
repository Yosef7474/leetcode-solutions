class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        
        target_sum = skill[0] + skill[-1]
        total_chemistry = 0
        
        for i in range(n // 2):
            left = skill[i]
            right = skill[n - 1 - i]
            
            # Check if this pair has the required sum
            if left + right != target_sum:
                return -1
            
            # Add the chemistry (product)
            total_chemistry += left * right
        
        return total_chemistry