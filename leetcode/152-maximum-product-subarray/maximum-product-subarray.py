class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        size = len(nums)
        maxm = nums[0]
        minm = nums[0]
        ans = nums[0]

        for i in range(1, size):
            temp = max(nums[i], nums[i] * maxm, nums[i] * minm)
            minm = min(nums[i], nums[i] * maxm, nums[i] * minm)
            maxm = temp
            ans = max(ans, maxm)

        return ans