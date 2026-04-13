class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        cnt = 0

        if len(s) < 3:
            return 0

        for i in range(len(s) - 2):
            sub = s[i:i + 3]
            if len(set(sub)) == 3:
                cnt += 1

        return cnt