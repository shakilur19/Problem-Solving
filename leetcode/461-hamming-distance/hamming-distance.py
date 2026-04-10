class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = 0
        val = x ^ y

        while val > 0:
            dist += 1
            val = val & (val - 1)

        return dist
        