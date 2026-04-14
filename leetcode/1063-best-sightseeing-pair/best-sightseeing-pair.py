class Solution:
    def maxScoreSightseeingPair(self, nums: List[int]) -> int:
        size = len(nums)
        maxm = nums[0]
        ans = 0

        for i in range(1, size):
            ans = max(ans, maxm + nums[i] - i)
            maxm = max(maxm, nums[i] + i)

        return ans