class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # Create dictionary of list1 with indices
        index_map = {}
        for i, restaurant in enumerate(list1):
            index_map[restaurant] = i
        
        min_sum = float('inf')
        result = []
        
        # Check list2
        for j, restaurant in enumerate(list2):
            if restaurant in index_map:
                i = index_map[restaurant]
                current_sum = i + j
                
                if current_sum < min_sum:
                    min_sum = current_sum
                    result = [restaurant]
                elif current_sum == min_sum:
                    result.append(restaurant)
        
        return result