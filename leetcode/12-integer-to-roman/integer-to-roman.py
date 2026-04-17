class Solution:
    def intToRoman(self, num: int) -> str:
        mp = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        n = num
        arr = []
        pos = 0

        while n > 0:
            rem = n % 10
            pos += 1
            arr.append((rem, pos))
            n //= 10

        res = ""

        for i in range(len(arr) - 1, -1, -1):
            digit = arr[i][0]
            base = 10 ** (arr[i][1] - 1)
            if digit <= 3:
                res += mp[base] * digit
            elif digit == 4:
                res += mp[base] + mp[5 * base]
            elif digit == 5:
                res += mp[5 * base]
            elif digit <= 8:
                res += mp[5 * base] + mp[base] * (digit - 5)
            elif digit == 9:
                res += mp[base] + mp[10 * base]

        return res