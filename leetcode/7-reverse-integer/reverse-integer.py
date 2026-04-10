class Solution:
    def isEx(self, x: int) -> bool:
        m = 2 ** 31 -1
        n = -2**31
        return n <= x <= m
    def reverse(self, x: int) -> int:
        
        y = abs(x)
        rev = 0
        while(y != 0):
            reminder = y % 10
            rev = rev * 10 + reminder
            y = y // 10

        if self.isEx(rev):
            if x < 0:
                return -1 * rev
            else:
                return rev
        
        return 0