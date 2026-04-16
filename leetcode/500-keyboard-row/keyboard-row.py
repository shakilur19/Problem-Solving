class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"
        ans = []
        
        for word in words:
            ans_word = ""
            for char in word:
                if char.lower() in first:
                    ans_word += char
                else:
                    break
            if ans_word == word:
                ans.append(word)

        for word in words:
            ans_word = ""
            for char in word:
                if char.lower() in second:
                    ans_word += char
                else:
                    break
            if ans_word == word:
                ans.append(word)
        
        for word in words:
            ans_word = ""
            for char in word:
                if char.lower() in third:
                    ans_word += char
                else:
                    break
            if ans_word == word:
                ans.append(word)
        return ans
        