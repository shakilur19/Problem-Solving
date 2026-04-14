class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t1Len = len(s)
        mainString = s
        rev = s[::-1]

        vec = [[0] * (t1Len + 1) for _ in range(t1Len + 1)]

        for i in range(t1Len - 1, -1, -1):
            for j in range(t1Len - 1, -1, -1):
                if mainString[i] == rev[j]:
                    vec[i][j] = 1 + vec[i + 1][j + 1]
                else:
                    vec[i][j] = max(vec[i][j + 1], vec[i + 1][j])

        return vec[0][0]