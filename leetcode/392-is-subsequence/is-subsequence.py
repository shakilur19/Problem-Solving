class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 or s is None: return True

        current = 0

        for i in range(0, len(t)):
            if s[current] == t[i]:
                current += 1
                if current == len(s):
                    return True

        return False
        