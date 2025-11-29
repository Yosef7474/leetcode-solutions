class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()  # Sort to enable early pruning
        
        def backtrack(start, current_combination, remaining):
            if remaining == 0:
                result.append(current_combination.copy())
                return
            
            for i in range(start, len(candidates)):
                # Early pruning: if candidate is too large, skip rest
                if candidates[i] > remaining:
                    break
                
                current_combination.append(candidates[i])
                backtrack(i, current_combination, remaining - candidates[i])
                current_combination.pop()
        
        backtrack(0, [], target)
        return result