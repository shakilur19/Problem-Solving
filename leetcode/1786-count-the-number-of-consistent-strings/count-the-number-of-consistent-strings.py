class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        counter = 0
        for word in words:
            word_set = set(word)
            common = word_set & allowed_set 
            if len(common) == len(word_set):
                counter += 1
            
        return counter
        