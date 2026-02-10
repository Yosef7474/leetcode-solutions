class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"), 
            set("zxcvbnm")
        ]
        
        result = []
        
        for word in words:
            lowercase_word = word.lower()
            for row in rows:
                if lowercase_word[0] in row:
                    if all(char in row for char in lowercase_word):
                        result.append(word)
                    break
        
        return result