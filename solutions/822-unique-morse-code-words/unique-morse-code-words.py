class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        transformations = set()
        
        for word in words:
            morse_word = ""
            for char in word:
                morse_word += morse_codes[ord(char) - ord('a')]
            transformations.add(morse_word)
        
        return len(transformations)