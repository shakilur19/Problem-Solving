class Solution:
    def maxSum(self, nums: List[int]) -> int:
        size = len(nums)
        total = 0

        maxm = nums[0]
        minm = nums[0]
        maxTill = nums[0]
        minTill = nums[0]

        if size == 1:
            return nums[0]

        for num in nums:
            total += num

        for i in range(1, size):
            maxm = max(nums[i] + maxm, nums[i])
            maxTill = max(maxTill, maxm)

            minm = min(nums[i] + minm, nums[i])
            minTill = min(minTill, minm)

        return max(maxTill, total - minTill)

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        size = len(nums)
        negativeCounter = 0

        for i in range(size):
            if nums[i] < 0:
                negativeCounter += 1

        if negativeCounter == size:
            nums.sort(reverse=True)
            return nums[0]

        return self.maxSum(nums)