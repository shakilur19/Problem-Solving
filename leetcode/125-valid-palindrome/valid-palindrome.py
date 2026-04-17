class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for c in s:
            c = c.lower()
            if (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9')):
                st += c
        i = 0
        j = (len(st) -1)
        while i < j:
            if st[i] == st[j]:
                i += 1
                j -= 1
            else:
                return False
        return True