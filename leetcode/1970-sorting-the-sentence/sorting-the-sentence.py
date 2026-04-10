class Solution:
    def sortSentence(self, s: str) -> str:
        splited = s.split(" ")
        ans = [None]* len(splited)

        for word in splited:
            actual_word = word[0:len(word) -1]
            digit = word[len(word) -1:len(word)]
            print(digit)
            ans[int(digit)- 1] = actual_word
        
        return " ".join(ans)
        