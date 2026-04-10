class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        ans = {}
        for i in words:
            ans[i] = ans.get(i, 0) + 1
        res = sorted(ans, key = ans.get, reverse=True)
        return res[0:k]
        