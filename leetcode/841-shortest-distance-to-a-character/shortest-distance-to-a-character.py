class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = [float('inf')] * len(s)

        for i in range(len(s)):
            if s[i] == c:
                ans[i] = 0
            elif i > 0:
                ans[i] = ans[i - 1] + 1

        for i in range(len(s) - 2, -1, -1):
            ans[i] = min(ans[i], ans[i + 1] + 1)

        return ans