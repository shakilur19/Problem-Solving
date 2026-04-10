class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        adj = ord(s[0])
        for i in s:
            sum = sum + abs(adj - ord(i))
            adj = ord(i)
        return sum
        