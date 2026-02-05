class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_count = [float('inf')] * 26
        
        for word in words:
            current_count = [0] * 26
            for char in word:
                current_count[ord(char) - ord('a')] += 1
            
            for i in range(26):
                common_count[i] = min(common_count[i], current_count[i])
        
        result = []
        for i in range(26):
            for _ in range(common_count[i]):
                result.append(chr(ord('a') + i))
        
        return result