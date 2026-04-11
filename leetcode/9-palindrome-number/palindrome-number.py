class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        reverse = 0
        i = 0
        if x < 0:
            return False
        while n > 0:
            reminder = n % 10
            reverse = (reverse * 10) + reminder
            n = n//10
  
        return reverse == x


        