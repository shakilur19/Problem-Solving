class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_lenght = len(needle)
        h_length = len(haystack)

        for i in range(h_length):
            if needle == haystack[i:i+n_lenght]:
                return i

        return -1
        