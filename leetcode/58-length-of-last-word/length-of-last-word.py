class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        lst = []
        for word in words:
            if word != '':
                lst.append(word)

        return len(lst[-1])
        