class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for c in s:
            c = c.lower()
            if (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9')):
                st += c
        
        return st == st[::-1]