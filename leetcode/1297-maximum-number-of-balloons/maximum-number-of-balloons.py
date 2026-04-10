class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char = [0] * 26

        for ch in text:
            char[ord(ch) - ord('a')] += 1

        b = char[ord('b') - ord('a')]
        a = char[ord('a') - ord('a')]
        l = char[ord('l') - ord('a')] // 2
        o = char[ord('o') - ord('a')] // 2
        n = char[ord('n') - ord('a')]

        return min(b, a, l, o, n)