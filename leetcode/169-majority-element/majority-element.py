class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = {}
        for i in nums:
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1
        return max(ans, key=ans.get)
        