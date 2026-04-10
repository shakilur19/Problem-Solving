class Solution:
    def addToArrayForm(self, digits: List[int], k: int) -> List[int]:
        digits[-1] = digits[-1] + k
        arr = []
        length = len(digits) - 1
        val = 0

        while length != -1:
            val += digits[length]
            val, reminder = divmod(val, 10)
            arr.append(reminder)
            length -= 1

        while val > 0:
            val, reminder = divmod(val, 10)
            arr.append(reminder)
        return arr[::-1]
        