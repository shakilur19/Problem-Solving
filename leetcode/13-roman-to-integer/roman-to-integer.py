class Solution:
    def romanToInt(self, roman: str) -> int:
        myMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        length = len(roman)
        total = myMap[roman[length - 1]]

        for i in range(length - 2, -1, -1):
            a = myMap[roman[i]]
            b = myMap[roman[i + 1]]

            if a < b:
                total -= a
            else:
                total += a

        return total